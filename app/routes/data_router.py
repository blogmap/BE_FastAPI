from fastapi import APIRouter, HTTPException
from app.models.search_request import SearchRequest
from app.services.qdrant_service import search_in_qdrant, store_data_in_qdrant, create_new_collection
from app.load_wiki_data import load_wikipedia_data
router = APIRouter()
from app.models.store_request import StoreRequest
@router.post("/store_wiki_data")
async def store_wiki_data(request: StoreRequest):
    try:
        new_collection = request.collection_name
        titles, texts = load_wikipedia_data(request.limit)
        create_new_collection(new_collection)
        store_data_in_qdrant(new_collection, titles, texts)
        return {
             "message": f"Lưu thành công vào collection {request.collection_name}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
