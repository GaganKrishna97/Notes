from fastapi import FastAPI, HTTPException
from mod import Book
import crud

app = FastAPI()

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    return crud.create_book(book)

@app.get("/books/", response_model=list[Book])
def list_books():
    return crud.list_books()

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = crud.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, new_book: Book):
    updated = crud.update_book(book_id, new_book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    deleted = crud.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"msg": "Book deleted"}
