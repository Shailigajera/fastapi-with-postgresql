from model import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

def create_book(db:Session, data:BookCreate):
    book_instance = Book(**data.model_dump())
    db.add(book_instance) 
    db.commit()
    db.refresh(book_instance)

    return book_instance


def get_book(db:Session):
    return db.query(Book).all()

def get_books(db:Session , id :int):
    return db.query(Book).filter(Book.id==id).first()
