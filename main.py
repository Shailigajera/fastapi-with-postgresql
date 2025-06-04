from fastapi import  FastAPI , Depends, Exception
import services, model, schemas
from db import get_db, engine
from sqlachemy.orm import Session

app=FastAPI()

@app.get("/books" , response_model=list[schemas.Book])