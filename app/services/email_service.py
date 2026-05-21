import httpx
from app.core.config import RESEND_API_KEY, TEST_EMAIL


async def send_email_test(task_title: str):
    async with httpx.AsyncClient() as client:
        await client.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "from": "onboarding@resend.dev",
                "to": [TEST_EMAIL],
                "subject": "Task completed ✅",
                "html": f"<p>You completed: {task_title}</p>"
            }
        )