from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, field_validator
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
    id: str
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

@field_validator("title")
def tittle_cannot_be_whitespase(cls,v):
    if not v.strip():
     return ValueError