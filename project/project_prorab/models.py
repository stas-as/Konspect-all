from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)         #почта
    password = Column(String)                               #пароль
    is_active = Column(Boolean, default=True)               #активность
    created_at = Column(DateTime, default=datetime.utcnow)  #дата_создания
    group = Column(String)                                  #группа

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)                                               #описание
    description = Column(Text)
    status = Column(String, default="open")                                          #статус
    priority = Column(String)                                                        #приоритет
    category = Column(String)                                                        #категория
    responsible_user_id = Column(Integer, ForeignKey('users.id'))                    #ответственный
    author_user_id = Column(Integer, ForeignKey('users.id'))                         #автор
    created_at = Column(DateTime, default=datetime.utcnow)                           #дата_создания
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) #дата_обновления

    responsible_user = relationship('User', foreign_keys=[responsible_user_id])
    author_user = relationship('User', foreign_keys=[author_user_id])

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    author_user_id = Column(Integer, ForeignKey('users.id'))
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    author_user = relationship('User')
    ticket = relationship('Ticket')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(Text)


"""
3. Схемы для валидации данных с использованием Pydantic
Для валидации входных данных мы будем использовать Pydantic.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    password: str
    group: Optional[str] = "user"

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime
    group: str

    class Config:
        orm_mode = True

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str
    category: str
    responsible_user_id: int

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    category: str
    responsible_user_id: int
    author_user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    text: str
    author_user_id: int

class CommentResponse(BaseModel):
    id: int
    text: str
    author_user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CategoryCreate(BaseModel):
    name: str
    description: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True