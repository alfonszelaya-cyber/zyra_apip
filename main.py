from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.status import router as status_router

app = FastAPI(
    title="ZYRA API",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"Zyra": "Sistema Limpio Online"}

app.include_router(health_router)
app.include_router(status_router)
