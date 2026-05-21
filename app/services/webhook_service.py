import httpx

WEBHOOK_URL = "https://webhook.site/9ea0bfab-0563-4803-ac81-2b7070a8b437"

async def send_webhook(event: str, data: dict):
    payload = {
        "event": event,
        "data": data
    }

    async with httpx.AsyncClient() as client:
        try: 
            await client.post(WEBHOOK_URL, json=payload)
        except Exception as e:
            print("Webhook failed:", e)