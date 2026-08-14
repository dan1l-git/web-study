from pydantic import BaseModel, ConfigDict
from api.enums.status import TaskStatus

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None

class TaskResponse(TaskBase):
    id: int
    status: TaskStatus
    model_config = ConfigDict(from_attributes=True)