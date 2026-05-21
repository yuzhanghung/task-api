from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class Task(BaseModel):
    id: UUID
    user_id: Optional[UUID] = None
    title: str
    completed: bool
    created_at: datetime