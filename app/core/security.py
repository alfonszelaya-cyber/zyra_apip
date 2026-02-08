from fastapi import Request
from datetime import datetime
import logging
from passlib.context import CryptContext

# ===== LOGGER =====
logger = logging.getLogger("ZYRA_SECURITY")

# ===== PASSWORD CONTEXT =====
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# ===== PASSWORD FUNCTIONS =====
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

# ===== REQUEST LOGGER MIDDLEWARE =====
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
