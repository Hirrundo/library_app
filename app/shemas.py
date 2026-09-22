from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, field_validator
from enum import Enum


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    genre: str
    description: str
    shortDescription:str
    readsCount:int
    likesCount:int

class BookDetial(BaseModel):
    isAvailable:bool
    reader_name:Optional[str]

class Reader(BaseModel):
    id: int
    fullName: str
    email: str
    phone: str
    registrationDate:str

class BookHistory(BaseModel):
    bookId:int
    takenAt:str
    returnedAt:Optional[str]
class ReaderProfile(BaseModel):
    reading_history:List[Book]

class UserBase(BaseModel):
  username: str
  email: EmailStr
  role: str = "librarian"
class UserCreate(UserBase):
    password: str
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    reader_id: Optional[int] = None

class Config:
    from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None
class LoginRequest(BaseModel):
    username: str
    password: str


@field_validator("title")
def tittle_cannot_be_whitespase(cls,v):
    if not v.strip():
     return ValueError