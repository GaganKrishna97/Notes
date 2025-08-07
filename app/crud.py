from sqlalchemy.orm import Session
from models import Note, NoteCreate

def create_note(db: Session, note: NoteCreate) -> Note:
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def get_notes(db: Session):
    return db.query(Note).all()

def update_note(db: Session, note_id: int, note: NoteCreate):
    db_note = get_note(db, note_id)
    if db_note:
        db_note.title = note.title
        db_note.content = note.content
        db.commit()
        db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = get_note(db, note_id)
    if db_note:
        db.delete(db_note)
        db.commit()
        return True
    return False
