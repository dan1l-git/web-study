from api.models.task import Task
from sqlalchemy.orm import Session
from api.schemas.task import TaskCreate, TaskUpdate
from api.enums.status import TaskStatus
from api.exceptions.task_exceptions import TaskNotFoundError

class TaskRepository:
    def get_all(self, db: Session, status: TaskStatus | None = None):
        if status:
            return db.query(Task).filter(Task.status == status).all()
        return db.query(Task).all()

    def create(self, db: Session, task_in: TaskCreate):
        db_task = Task(**task_in.model_dump())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return db_task

    def update(self, db: Session, task_id: int, task_in: TaskUpdate):
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if not db_task:
            raise TaskNotFoundError(f"Task with id {task_id} not found")

        update_data = task_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_task, key, value)

        db.commit()
        db.refresh(db_task)
        return db_task

    def delete(self, db: Session, task_id: int):
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if not db_task:
            raise TaskNotFoundError(f"Task with id {task_id} not found")

        db.delete(db_task)
        db.commit()
        return True