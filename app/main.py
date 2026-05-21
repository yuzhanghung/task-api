from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.tasks import router as tasks_router


app = FastAPI(title="Task API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def home():
    return {"message": "Task API is running"}


app.include_router(tasks_router)