from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(
    title="ZYRA API",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"Zyra": "Sistema Limpio Online"}

# Inyecta la ruta health desde app/routes
app.include_router(health_router)
