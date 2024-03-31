from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    name: str
    description: str | None

@app.get("/tasks")
def get_task():
    task = Task(name="Loading this video")
    return {"data": task}

