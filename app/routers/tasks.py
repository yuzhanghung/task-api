from fastapi import APIRouter
from app.models.task import TaskCreate, TaskUpdate
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("")
async def get_tasks():
    return await task_service.get_tasks()


@router.post("")
async def create_task(task: TaskCreate):
    return await task_service.create_task(task)

@router.patch("/{task_id}")
async def update_task(task_id: str, updates: TaskUpdate):
    return await task_service.update_task(task_id, updates)

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    return await task_service.delete_task(task_id)