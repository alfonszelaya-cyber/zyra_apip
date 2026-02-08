from fastapi import FastAPI
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.core.security import log_request

def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title=settings.app_name,
        version=settings.version
    )

    @app.middleware("http")
    async def security_middleware(request, call_next):
        return await log_request(request, call_next)

    return app
