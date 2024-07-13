from pydantic import BaseModel, ConfigDict, Field, ValidationError


class Proxy(BaseModel):
    id: str
    ip: str
    port: str
    user: str
    password: str = Field(validation_alias='pass')

class ListProxy(BaseModel):
    items : dict[str,Proxy] = Field(validation_alias='list')
    list_count : int
