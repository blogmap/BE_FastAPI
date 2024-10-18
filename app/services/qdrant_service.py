from app.models.sentence_transformer import load_model
from qdrant.qdrant_service import create_collection, insert_embeddings, search_embeddings

# Đường dẫn đến mô hình
model_path = "C:\\Users\\Admin\\Desktop\\New folder\\New folder\\MindMap\\saved_model"
model = load_model(model_path)

# Hàm tạo collection Qdrant cho Wikipedia embeddings
def create_new_collection(collection_name):
    try:
        vector_size = model.get_sentence_embedding_dimension()
        create_collection(collection_name, vector_size)
        print(f"Collection '{collection_name}' đã được tạo thành công với kích thước vector {vector_size}")
    except Exception as e:
        print(f"Lỗi khi tạo collection: {str(e)}")

# Hàm thêm dữ liệu vào Qdrant
def store_data_in_qdrant(collection_name, titles, texts):
    try:
        # Mã hóa các texts để lấy embeddings
        wiki_embeddings = model.encode(texts)
        payloads = [{"title": title, "text": text} for title, text in zip(titles, texts)]
        
        # Thêm embeddings và payloads vào collection
        insert_embeddings(collection_name, wiki_embeddings, payloads)
        print(f"Đã lưu thành công dữ liệu vào collection '{collection_name}'")
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu vào Qdrant: {str(e)}")

# Hàm tìm kiếm trong Qdrant
def search_in_qdrant(collection_name, content):
    try:
        # Mã hóa câu tìm kiếm để lấy embedding
        search_embedding = model.encode([content])[0]
        
        # Tìm kiếm trong collection đã cho
        results = search_embeddings(collection_name, search_embedding)
        return results
    except Exception as e:
        print(f"Lỗi khi tìm kiếm trong Qdrant: {str(e)}")
        return None
