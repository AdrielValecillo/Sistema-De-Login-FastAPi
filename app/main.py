from fastapi import FastAPI
from app.api.routers import auth
from app.db.database import Base, engine
from app.api.routers import tasks
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Crear tablas
Base.metadata.create_all(bind=engine)

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Hello World"}

# Incluir rutas
app.include_router(auth.router)
app.include_router(tasks.router)
