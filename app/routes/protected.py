from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import decode_token

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)

security = HTTPBearer()


# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔐 Endpoint protegido
@router.get("/")
def protected_route(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    email = payload.get("sub")
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return {
        "message": "Access granted",
        "user": user.email
    }
