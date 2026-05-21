from app.services.callback import register_task_completed_callback
from app.services.email_service import send_email_test

async def email_on_task_completed(task: dict):
    await send_email_test(task["title"])

register_task_completed_callback(email_on_task_completed)