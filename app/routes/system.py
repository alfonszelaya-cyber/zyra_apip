from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/system", tags=["System"])

@router.get("/info")
def system_info():
    return {
        "system": "ZYRA API",
        "status": "operational",
        "timestamp": datetime.utcnow().isoformat()
    }
