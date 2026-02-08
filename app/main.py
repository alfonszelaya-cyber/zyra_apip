from app.core.application import create_app
from app.routes.health import router as health_router
from app.routes.status import router as status_router
from app.routes.system import router as system_router

app = create_app()

@app.get("/")
def read_root():
    return {
        "Zyra": "Sistema Limpio Online"
    }

app.include_router(health_router)
app.include_router(status_router)
app.include_router(system_router)
