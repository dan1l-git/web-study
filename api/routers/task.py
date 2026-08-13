from fastapi import APIRouter, Depends
from api.database import get_db
from sqlalchemy.orm import Session
from api.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from api.enums.status import TaskStatus
from api.repository.task import TaskRepository
from api.services.task import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_task_service():
    task_repository = TaskRepository()
    return TaskService(task_repository)

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), service: TaskService = Depends(get_task_service)):
    return service.create_task(db=db, task=task)

@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db), service: TaskService = Depends(get_task_service), status: TaskStatus | None = None):
    return service.get_tasks(db=db, status=status)

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), service: TaskService = Depends(get_task_service)):
    return service.update_task(db=db, task_id=task_id, task=task)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), service: TaskService = Depends(get_task_service)):
    service.delete_task(db=db, task_id=task_id)
    return {"detail": f"Task #{task_id} deleted successfully"}
