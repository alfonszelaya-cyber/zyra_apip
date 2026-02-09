from passlib.context import CryptContext

from app.routes.protected import router as protected_router
from app.core.application import create_app
from app.routes.health import router as health_router
from app.routes.status import router as status_router
from app.routes.system import router as system_router
from app.routes.users import router as users_router
from app.routes.auth import router as auth_router  # ✅ INYECTADO
from app.db.session import init_db
from app.core.security import log_request  # ✅ Ya estaba

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = create_app()

# ✅ Middleware Seguridad / Logging
app.middleware("http")(log_request)

# Inicializa base de datos
init_db()

@app.get("/")
def read_root():
    return {
        "Zyra": "Sistema Limpio Online"
    }

app.include_router(health_router)
app.include_router(status_router)
app.include_router(system_router)
app.include_router(users_router)
app.include_router(auth_router)  # ✅ INYECTADO
app.include_router(protected_router)
