from fastapi import FastAPI
from routers import task
from routers import user
from backend.db import engine
from app.models import User, Task


app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)
