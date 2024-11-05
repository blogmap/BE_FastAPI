from datasets import load_dataset

def load_wikipedia_data(num_items):
    dataset = load_dataset("wikipedia", "20220301.en", split="train")
    print(f"Số lượng item trong dataset: {len(dataset)}")
    titles = [dataset[i]['title'] for i in range(num_items)]  
    texts = [dataset[i]['text'] for i in range(num_items)]   
    
    return titles, texts
