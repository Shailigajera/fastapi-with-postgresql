from model import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

def create_book(db:Session, data:BookCreate):
    book_instance = Book.(**data.model_dump())
    db.add(boook_instance) 
    db.commit()
    db.refresh()

    return book_instance


def get_books(db:Session):
    return db.query(Book).all()