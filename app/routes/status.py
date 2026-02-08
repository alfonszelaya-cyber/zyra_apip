from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/status")
def status():
    return {
        "system": "ZYRA",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat()
    }
