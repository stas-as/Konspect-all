from typing import Annotated, List
from fastapi import FastAPI, Path, Query, status, Body, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

from pydantic import BaseModel

templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    id: int | None = None
    text: str
    
    model_config = {
        "json_schema_extra": {
            "examples":
                [
                    {
                        "text": "Simple message",
                    }
                ]
        }
    }


messages_db = []



@app.get("/")
async def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "message.html", {"messages": messages_db})


@app.get("/message/{message_id}")
async def get_message(message_id: int) -> Message:
    try:
        return messages_db[message_id] 
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message(message: Message) -> str:
    if messages_db:
        message.id = max(messages_db, key = lambda x: x.id).id +1
    else:
        message.id = 0
    messages_db.append(message)
    return f"Message created!"


@app.put("/message/{message_id}")
async def update_message(message_id: int, message: str = Body()) -> str:
    try:
        edit_message = messages_db[message_id]
        edit_message.text = message
        return "Message updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/message/{message_id}")
async def delete_message(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f"Message ID={message_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/")
async def kill_message_all() -> str:
    messages_db.clear()
    return "All messages deleted!"






























# @app.get("/user")
# async def search(people: Annotated[list[str], Query()]) -> dict:
#     return {"user": people}

# @app.get("/user/{name}")
# async def user(name: str = Path(min_length=4, max_length=20, description='Enter your name')) -> dict:
#     return {'user_name': name}


# @app.get("/employee/{name}/company/{company}")
# async def eployee(name: str,department: str, company: str ) -> dict:
#     return {"name": name, "company": company, "department": department}

# @app.get("/employee/{name}/company/{company}")
# async def get_employee(name: str, department: str, company: str) -> dict:
#     return {"Employee": name, "Company": company, "Department": department}

# @app.get("/")
# async def welcome() -> dict:
#     return {"message": f"Hello world"}


# @app.get("/hello/{first_name}/{last_name}")
# async def welcome_user(first_name: str, last_name: str) -> dict:
#     return {"message": f"Hello {first_name} {last_name}"}


# @app.get("/order/{id}")
# async def order(id: int) -> dict:
#     return {"order": f"{id}"}

