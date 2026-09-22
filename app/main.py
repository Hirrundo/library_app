from fastapi import FastAPI
from typing import List
from shemas import Book, Reader
from data import books,readers
from auth_routes import router
app = FastAPI()

@app.get('/books',response_model=List[Book])
def return_books():
    return books

@app.get('/readers', response_model=List[Reader])
def return_readers():
    return readers

@app.get('/readers/{reader_id}', response_model=Reader)
def return_readerProfile(reader_id):
    for reader in readers:
        if reader['id']==reader_id:
            return reader

@app.get('/books/{book_id}',response_model=Book)
def return_book(book_id):
    for book in books:
        if book['id']==book_id:
            return book
