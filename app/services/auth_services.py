from fastapi import HTTPException, status
from app.api.utils.utils import hash_password, verify_password, create_access_token
from app.db.models.models import Usuario
from datetime import timedelta

ACCESS_TOKEN_EXPIRE_MINUTES = 30
class UserServices:
    def authenticate_user(serf, username: str, password: str, db):
        usuario = db.query(Usuario).filter(Usuario.username == username).first()
        if not usuario or not verify_password(password, usuario.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas",
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token({"sub": usuario.username}, expires_delta=access_token_expires)
        return {"access_token": token, "token_type": "bearer"}


    def register_user(self, username: str, email: str, password: str, db):
        user_exists = db.query(Usuario).filter(Usuario.email == email).first()
        if user_exists:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
        
        password_hash = hash_password(password)
        usuario = Usuario(username=username, email=email, password_hash=password_hash)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
