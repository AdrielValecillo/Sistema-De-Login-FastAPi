from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.models.models import Tarea, Usuario
from app.db.schemas.shemas import TareaCreate, TareaResponse
from app.db.database import get_db
from app.api.utils.utils import get_current_user

router = APIRouter()

@router.get("/tasks", response_model=list[TareaResponse])
def get_tasks(db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return db.query(Tarea).filter(Tarea.usuario_id == current_user.id).all()

@router.post("/tasks", response_model=TareaResponse)
def create_task(task: TareaCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    nueva_tarea = Tarea(**task.dict(), usuario_id=current_user.id)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea
