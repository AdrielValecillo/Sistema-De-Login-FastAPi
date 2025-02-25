from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.api.utils.utils import hash_password, verify_password, create_access_token
from app.db.models.models import Usuario


def authenticate_user(username: str, password: str, db: Session):
    usuario = db.query(Usuario).filter(Usuario.username == username).first()
    if not usuario or not verify_password(password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    token = create_access_token({"sub": usuario.username})
    return {"access_token": token, "token_type": "bearer"}

def register_user(username: str, email: str, password: str, db: Session):
    user_exists = db.query(Usuario).filter(Usuario.email == email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    password_hash = hash_password(password)
    usuario = Usuario(username=username, email=email, password_hash=password_hash)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario