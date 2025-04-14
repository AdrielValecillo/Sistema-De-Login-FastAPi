from sqlalchemy.orm import Session
from app.db.models.models import Tarea, Usuario
from app.db.schemas.shemas import TareaCreate

def get_user_tasks(db: Session, current_user: Usuario):
    return db.query(Tarea).filter(Tarea.owner_id == current_user.id).all()

def create_new_task(task: TareaCreate, db: Session, current_user: Usuario):
    new_task = Tarea(**task.dict(), owner_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task