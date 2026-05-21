from starlette.concurrency import run_in_threadpool
from app.db.supabase import supabase
from app.models.task import TaskCreate, TaskUpdate
from app.services.webhook_service import send_webhook

async def get_tasks():
    def query():
        return supabase.table("tasks").select("*").order("created_at", desc=True).execute()
    
    response = await run_in_threadpool(query)
    return response.data

async def create_task(task: TaskCreate):
    def query():
        return supabase.table("tasks").insert(task.model_dump()).execute()
    
    response = await run_in_threadpool(query)
    data = response.data

    await send_webhook("task.created", data)
    return data


async def update_task(task_id: str, updates: TaskUpdate):
    data = updates.model_dump(exclude_none=True)

    def query():
        return supabase.table("tasks").update(data).eq("id", task_id).execute()
    
    response = await run_in_threadpool(query)
    return response.data

async def delete_task(task_id: str):
    def query():
        return supabase.table("tasks").delete().eq("id", task_id).execute()
    
    response = await run_in_threadpool(query)
    return response.data