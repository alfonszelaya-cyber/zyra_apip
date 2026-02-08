from fastapi import Request
from datetime import datetime
import logging

logger = logging.getLogger("ZYRA_SECURITY")

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
