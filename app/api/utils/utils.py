from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.models.models import Usuario
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

oauth2_scheme = HTTPBearer()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return db.query(Usuario).filter(Usuario.username == username).first()
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")