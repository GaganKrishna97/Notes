from sqlalchemy.orm import Session
import crud
from typing import List

class UserService:
    @staticmethod
    def create_user(db: Session, username: str):
        user = crud.get_user_by_username(db, username)
        if user:
            raise ValueError("Username already exists")
        return crud.create_user(db, username)

    @staticmethod
    def get_user(db: Session, user_id: int):
        user = crud.get_user(db, user_id)
        if not user:
            raise ValueError("User not found")
        return user

class NoteService:
    @staticmethod
    def create_note(db: Session, owner_id: int, title: str, content: str, tags: List[str]):
        if not title or not content:
            raise ValueError("Title and content cannot be empty")
        return crud.create_note(db, owner_id, title, content, tags)

    @staticmethod
    def get_note(db: Session, note_id: int):
        note = crud.get_note(db, note_id)
        if not note:
            raise ValueError("Note not found")
        return note

    @staticmethod
    def get_notes(db: Session, owner_id: int = None):
        return crud.get_notes(db, owner_id)

    @staticmethod
    def update_note(db: Session, note_id: int, title: str, content: str, tags: List[str]):
        note = crud.update_note(db, note_id, title, content, tags)
        if not note:
            raise ValueError("Note not found")
        return note

    @staticmethod
    def delete_note(db: Session, note_id: int):
        if not crud.delete_note(db, note_id):
            raise ValueError("Note not found")
        return True

class TagService:
    @staticmethod
    def get_tags(db):
        return crud.get_tags(db)
