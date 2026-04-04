from fastapi import APIRouter

router = APIRouter()

@router.get("/analytics")
def get_stats():
    return {
        "total_alerts": 5,
        "resources_used": 20,
        "active_cases": 3
    }