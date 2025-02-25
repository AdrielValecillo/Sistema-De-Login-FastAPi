from fastapi import FastAPI
from app.api.routers import auth
from app.db.database import Base, engine
from app.api.routers import tasks
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Crear tablas
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
