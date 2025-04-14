from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.auth_services import UserServices
from app.api.utils.utils import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.db.models.models import Usuario
from app.db.schemas.shemas import UsuarioCreate

router = APIRouter(prefix="/auth", tags=["auth"])

user_services = UserServices()
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/login")
def login_for_access_token(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    token = user_services.authenticate_user(form_data.username, form_data.password, db)
    return {
        "access_token": token["access_token"],
        "token_type": token["token_type"],
        "message": "Inicio de sesión exitoso",
        "status": True,
        "code": 200
    }


# Registro de usuario
@router.post("/register")
def register(user: UsuarioCreate, db: db_dependency):
    try:
        user = user_services.register_user(user.username, user.email, user.password, db)
        return {"status": True, "data": user, "message": "Usuario registrado", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": str(e), "code": 400}

# Obtener usuario autenticado
@router.get("/me")
def read_users_me(current_user: Usuario = Depends(get_current_user)):
    return {"username": current_user.username, "email": current_user.email, "id": current_user.id, "status": True, "message": "Usuario autenticado", "code": 200}

