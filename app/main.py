from fastapi import FastAPI
from app.routes.search_route import router as search_router
from app.routes.data_router import router as data_router
from app.load_wiki_data import load_wikipedia_data
from app.services.qdrant_service import search_in_qdrant, store_data_in_qdrant

app = FastAPI()

# Biến toàn cục để kiểm tra xem dữ liệu đã được tải chưa
data_loaded = False
# from datasets import load_dataset

# # Tải dataset từ Wikipedia
# dataset = load_dataset("wikipedia", "20220301.en", split="train")

# print(f"Số lượng item trong dataset: {len(dataset)}")

# @app.on_event("startup")
# async def startup_event():
#     global data_loaded
#     if not data_loaded:
#         titles, texts = load_wikipedia_data()
#         store_data_in_qdrant(titles, texts)
#         data_loaded = True  # Đánh dấu rằng dữ liệu đã được tải
#         print("Dữ liệu Wikipedia đã được lưu vào Qdrant.")

app.include_router(search_router)
app.include_router(data_router)

#Các route khác và cấu hình ở đây