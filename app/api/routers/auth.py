from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.auth_services import authenticate_user, register_user

router = APIRouter()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    try:
        login = authenticate_user(username, password, db)
        return {"status": True, "data": login, "message": "Login exitoso", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": str(e), "code": 401}


@router.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    try:
        user = register_user(username, email, password, db)
        return {"status": True, "data": user, "message": "Usuario registrado", "code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": str(e), "code": 400}