from fastapi import APIRouter
from app.models.task import TaskCreate, TaskUpdate
from app.services import task_service
from app.services.callback import trigger_task_completed

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("")
async def get_tasks():
    return await task_service.get_tasks()


@router.post("")
async def create_task(task: TaskCreate):
    return await task_service.create_task(task)

@router.patch("/{task_id}")
async def update_task(
    task_id: str, 
    updates: TaskUpdate,
):
    updated_task = await task_service.update_task(task_id, updates)

    if updates.completed is True and updated_task:
        task = updated_task[0]

        await trigger_task_completed(task)
    
    return updated_task
    


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    return await task_service.delete_task(task_id)