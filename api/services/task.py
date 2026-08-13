from sqlalchemy.orm import Session
from api.schemas.task import TaskCreate, TaskUpdate
from api.enums.status import TaskStatus
from api.repository.task import TaskRepository
from fastapi import HTTPException
from api.exceptions.task_exceptions import TaskNotFoundError

class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    def get_tasks(self, db: Session, status: TaskStatus | None = None):
        return self.task_repo.get_all(db=db, status=status)

    def create_task(self, db: Session, task: TaskCreate):
        return self.task_repo.create(db=db, task_in=task)

    def update_task(self, db: Session, task_id: int, task: TaskUpdate):
        try:
            return self.task_repo.update(db=db, task_id=task_id, task_in=task)
        except TaskNotFoundError as e:
            raise HTTPException(status_code=404, detail="Task not found") from e

    def delete_task(self, db: Session, task_id: int):
        try:
            return self.task_repo.delete(db=db, task_id=task_id)
        except TaskNotFoundError as e:
            raise HTTPException(status_code=404, detail="Task not found") from e