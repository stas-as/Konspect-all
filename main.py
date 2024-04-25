from fastapi import *
from pydantic import BaseModel
from typing import Optional
from typing import Annotated
app = FastAPI()

    
class StaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
    
class STask(StaskAdd):
    id : int

tasks = []
@app.post("/tasks")
async def add_task(task: Annotated[StaskAdd, Depends()]):
    tasks.append(task)
    return{"OK":True}


# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Loading this video")
#     return {"data": task}

