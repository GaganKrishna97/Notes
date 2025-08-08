from typing import List, Optional
from mod import Book
from database import books_db

def create_book(book: Book) -> Book:
    books_db.append(book)
    return book

def list_books() -> List[Book]:
    return books_db

def get_book(book_id: int) -> Optional[Book]:
    for book in books_db:
        if book.id == book_id:
            return book
    return None

def update_book(book_id: int, new_book: Book) -> Optional[Book]:
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = new_book
            return new_book
    return None

def delete_book(book_id: int) -> bool:
    for index, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[index]
            return True
    return False
