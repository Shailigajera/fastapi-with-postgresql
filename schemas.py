import pydantic import BaseModel

class BookBase(BaseModel):
    title : str
    description: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id : int

    class config:
        