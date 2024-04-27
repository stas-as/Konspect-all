from fastapi import *
from pydantic import BaseModel
from typing import Optional
from typing import Annotated
app = FastAPI()

from contextlib import asynccontextmanager
from datebase import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")

app = FastAPI(lifespan=lifespan)
    
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

