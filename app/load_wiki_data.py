from datasets import load_dataset

def load_wikipedia_data(num_items):
    # Tải dataset từ Wikipedia
    dataset = load_dataset("wikipedia", "20220301.en", split="train")
    
    # Sử dụng chỉ số thay vì truy cập theo tên trường
    titles = [dataset[i]['title'] for i in range(num_items)]  # Tải toàn bộ title
    texts = [dataset[i]['text'] for i in range(num_items)]   
    
    return titles, texts
