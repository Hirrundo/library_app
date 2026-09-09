from datetime import date

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, create_engine, func
from sqlalchemy.orm import declarative_base, relationship


engine=create_engine('sqlite:///library.db')

Base=declarative_base()

class Book(Base):
    __tablename__='books',
    id= Column(Integer,autoincrement=True,primary_key=True),
    title=Column(String,nullable=False),
    author =Column(String,nullable=False),
    isbn =Column(String, nullable=True),
    year =Column(Integer,nullable=True),
    genre =Column(String,nullable=False),
    available_copies =Column(Integer,default=1)

   
class Reader(Base):
    __tablename__='readers',
    id=Column(Integer,autoincrement=True,primary_key=True),
    full_name =Column(String,nullable=False),
    email  =Column(String,unique=True,nullable=False),
    phone  =Column(String,nullable=True),
    registration_date  =Column(Date, default= date.today)

    reader=relationship('ReaderBooks',back_populates='readerB')

class ReaderBooks(Base):
     __tablename__='readersb'
     id=Column(Integer,autoincrement=True,primary_key=True)
     reader_id =Column(Integer,autoincrement=True,primary_key=True)
     book_id=Column(Integer,autoincrement=True,primary_key=True)
     taken_at=Column(String)
     returned_at=Column(String)

     readerB=relationship('Reader', back_populates='reader')
Base.metadata.create_all(bind=engine)

# date_object=datetime.strptime(date_string, '%d.%m.%Y')