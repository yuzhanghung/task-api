import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

@app.get("/")
def home():
    return {"message": "Task API is running"}

@app.get("/debug")
def debug():
    return {
        "url_exists": SUPABASE_URL is not None,
        "key_exists": SUPABASE_SERVICE_KEY is not None
    }

@app.get("/tasks")
def get_tasks():
    try:
        response = supabase.table("tasks").select("*").execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}

@app.post("/tasks")
def create_task(task: dict):
    try: 
        response = supabase.table("tasks").insert(task).execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}


@app.patch("/tasks/{task_id}")
def update_task(task_id: str, updates: dict):
    response = supabase.table("tasks").update(updates).eq("id", task_id).execute()
    return response.data

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    response = supabase.table("tasks").delete().eq("id", task_id).execute()
    return response.data
