from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.status import router as status_router
from app.routes.system import router as system_router
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.core.security import log_request

setup_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.version
)

@app.middleware("http")
async def security_middleware(request, call_next):
    return await log_request(request, call_next)

@app.get("/")
def read_root():
    return {"Zyra": "Sistema Limpio Online"}

app.include_router(health_router)
app.include_router(status_router)
app.include_router(system_router)
