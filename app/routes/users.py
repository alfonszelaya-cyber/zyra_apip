from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext

from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import decode_token

# 🔐 Configuración de hash (Enterprise Ready)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

security = HTTPBearer()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# Dependency para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Crear usuario
@router.post("/")
def create_user(
    email: str,
    full_name: str,
    password: str,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=email,
        full_name=full_name,
        hashed_password=hash_password(password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "email": new_user.email,
        "full_name": new_user.full_name
    }


# Listar usuarios (🔒 protegido con JWT)
@router.get("/", response_model=List[dict])
def list_users(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name
        }
        for user in users
    ]
