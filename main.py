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
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

print("SUPABASE_URL:", os.getenv("SUPABASE_URL"))

@app.get("/tasks")
def get_tasks():
    try:
        response = supabase.table("tasks").select("*").execute()
        return {"tasks": response.data}
    except Exception as e:
        return {"error": str(e)}

@app.post("/tasks")
def create_task(task: dict):
    response = supabase.table("tasks").insert(task).execute()
    return response

@app.patch("/tasks/{task_id}")
def update_task(task_id: str, updates: dict):
    response = supabase.table("tasks").update(updates).eq("id", task_id).execute()
    return response.data

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    response = supabase.table("tasks").delete().eq("id", task_id).execute()
    return response.data
