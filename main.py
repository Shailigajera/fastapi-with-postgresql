from fastapi import  FastAPI , Depends, HTTPException, status
import services, model, schemas
from db import get_db, engine
from sqlalchemy.orm import Session

app=FastAPI()

@app.get("/books" , response_model=list[schemas.Book])
def get_all_books(db:Session = Depends(get_db)):
    return services.get_book(db)

@app.post("/books", response_model=schemas.Book)
def create_new_book(book:schemas.BookCreate , db:Session = Depends(get_db)):
    return services.create_book(db, book)


@app.get("/books/{id}",response_model=schemas.Book )
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    queryset = services.get_books(db , id)
    if queryset :
        return queryset
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

