


"""
4. Основной файл API с FastAPI
Теперь создадим основной файл для API с эндпоинтами, которые мы описали в задаче.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List
from passlib.context import CryptContext

from models import User, Ticket, Comment, Category, UserCreate, TicketCreate, CommentCreate, CategoryCreate, UserResponse, TicketResponse, CommentResponse, CategoryResponse

# Инициализация FastAPI
app = FastAPI()

# Создаем подключение к базе данных
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Инициализация хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Зависимость для работы с сессией
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт регистрации пользователя
@app.post("/auth/register/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, group=user.group)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Эндпоинт авторизации пользователя (упрощенная версия)
@app.post("/auth/login/")
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

# Эндпоинт создания категории
@app.post("/categories/add/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Эндпоинт создания тикета
@app.post("/tickets/add/", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

# Эндпоинт получения тикета по ID
@app.get("/tickets/{id}/", response_model=TicketResponse)
def get_ticket(id: int, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

# Эндпоинт удаления тикета
@app.delete("/tickets/delete/{id}/")
def delete_ticket(id: int, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(db_ticket)
    db.commit()
    return {"message": "Ticket deleted successfully"}

# Эндпоинт добавления комментария к тикету
@app.post("/tickets/{ticket_id}/comments/", response_model=CommentResponse)
def add_comment(ticket_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db_comment = Comment(**comment.dict(), ticket_id=ticket_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

