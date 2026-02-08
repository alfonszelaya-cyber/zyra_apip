from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.status import router as status_router
from app.routes.system import router as system_router
from app.core.logging_config import setup_logging
from app.core.security import log_request

# ===== CONFIG LOCAL SEGURA (SIN pydantic_settings) =====
APP_NAME = "ZYRA API"
APP_VERSION = "1.0.0"
APP_OWNER = "JAZA GLOBAL"
ARCHITECTURE_LEVEL = "Enterprise"
BUILD_TARGET = "10+ Years Stable"

# Inicializa logging
setup_logging()

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

# Middleware
@app.middleware("http")
async def security_middleware(request, call_next):
    return await log_request(request, call_next)

# Root
@app.get("/")
def read_root():
    return {
        "Zyra": "Sistema Limpio Online",
        "owner": APP_OWNER,
        "architecture": ARCHITECTURE_LEVEL,
        "target": BUILD_TARGET
    }

# Routers
app.include_router(health_router)
app.include_router(status_router)
app.include_router(system_router)
