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

def update_book(db : Session, book: BookCreate,  id :int):
    book_details =  db.query(Book).filter(Book.id==id).first()
    if book_details:
        for key,value in book.model_dump().items():
            setattr(book_details, key, value)
    db.commit()
    db.refresh(book_details)
    return book_details

def delete_book(db:Session , id:int):
    book_detail = db.query(Book).filter(Book.id==id).first()
    if book_detail :
            db.delete(book_detail)
            db.commit()
    return (book_detail)
             


