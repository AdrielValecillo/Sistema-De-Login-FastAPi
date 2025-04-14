from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.models.models import Usuario
from app.db.schemas.shemas import TareaCreate, TareaResponse
from app.db.database import get_db
from app.api.utils.utils import get_current_user
from app.services.task_services import get_user_tasks, create_new_task

router = APIRouter(prefix="/task", tags=["tasks"])

@router.get("/getTask", response_model=list[TareaResponse])
def get_tasks(db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return get_user_tasks(db, current_user)

@router.post("/createTask", response_model=TareaResponse)
def create_task(task: TareaCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return create_new_task(task, db, current_user)
