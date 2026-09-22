from fastapi import Depends
from sqlalchemy import select

from auth import get_password_hash
from shemas import UserCreate
from models import User,Book
from dependesis import get_db

from sqlalchemy.orm import Session

def get_books(db:Session=Depends(get_db)):
    data=db.query(Book)
    return data.all()

def create_user(user:UserCreate,db:Session=Depends(get_db)):
    new_user=User(
        username=user.username,
        email=user.email,
        password_hash=get_password_hash(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user