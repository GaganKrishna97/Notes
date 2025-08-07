import crud
from sqlalchemy.orm import Session
from models import NoteCreate

class NoteService:
    @staticmethod
    def create_note(db: Session, note_in: NoteCreate):
        if not note_in.title or not note_in.content:
            raise ValueError("Title and Content cannot be empty")
        return crud.create_note(db, note_in)

    @staticmethod
    def get_note(db: Session, note_id: int):
        note = crud.get_note(db, note_id)
        if not note:
            raise ValueError("Note not found")
        return note

    @staticmethod
    def get_notes(db: Session):
        return crud.get_notes(db)

    @staticmethod
    def update_note(db: Session, note_id: int, note_in: NoteCreate):
        note = crud.update_note(db, note_id, note_in)
        if not note:
            raise ValueError("Note not found")
        return note

    @staticmethod
    def delete_note(db: Session, note_id: int):
        if not crud.delete_note(db, note_id):
            raise ValueError("Note not found")
        return True
