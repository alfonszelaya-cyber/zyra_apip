from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.status import router as status_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version
)

@app.get("/")
def read_root():
    return {"Zyra": "Sistema Limpio Online"}

app.include_router(health_router)
app.include_router(status_router)
