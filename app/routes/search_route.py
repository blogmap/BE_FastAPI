from fastapi import APIRouter, HTTPException
from app.models.search_request import SearchRequest
from app.services.qdrant_service import search_in_qdrant

router = APIRouter()

@router.post("/search")
async def search(request: SearchRequest):
    try:
        results = search_in_qdrant(request.content)
        return {
            "results": [
                {
                    "title": result.payload['title'],
                    "url": f"https://en.wikipedia.org/wiki/{result.payload['title'].replace(' ', '_')}",
                    "similarity": result.score,
                    "text": result.payload['text']
                }
                for result in results
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
