from fastapi import Request
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import logging
import os

# =====================================================
# LOGGER
# =====================================================

logger = logging.getLogger("ZYRA_SECURITY")

# =====================================================
# CONFIGURACIÓN GLOBAL SEGURIDAD
# =====================================================

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_THIS_SUPER_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# =====================================================
# PASSWORD FUNCTIONS
# =====================================================

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

# =====================================================
# JWT FUNCTIONS
# =====================================================

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

# =====================================================
# REQUEST LOGGER MIDDLEWARE
# =====================================================

async def log_request(request: Request, call_next):
    start_time = datetime.utcnow()

    response = await call_next(request)

    process_time = (datetime.utcnow() - start_time).total_seconds()

    logger.info(
        f"{request.method} {request.url.path} "
        f"Status:{response.status_code} "
        f"Time:{process_time}s"
    )

    return response
