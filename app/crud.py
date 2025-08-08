from sqlalchemy.orm import Session
from models import User, Note, Tag
from typing import List

# --- User CRUD ---
def create_user(db: Session, username: str) -> User:
    user = User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()

# --- Note CRUD ---
def create_note(db: Session, owner_id: int, title: str, content: str, tag_names: List[str]) -> Note:
    note = Note(title=title, content=content, owner_id=owner_id)
    tags = []
    for tag_name in tag_names:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
            db.add(tag)
            db.commit()
            db.refresh(tag)
        tags.append(tag)
    note.tags = tags

    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_note(db: Session, note_id: int) -> Note:
    return db.query(Note).filter(Note.id == note_id).first()

def get_notes(db: Session, owner_id: int = None) -> List[Note]:
    query = db.query(Note)
    if owner_id:
        query = query.filter(Note.owner_id == owner_id)
    return query.all()

def update_note(db: Session, note_id: int, title: str, content: str, tag_names: List[str]) -> Note:
    note = get_note(db, note_id)
    if not note:
        return None
    note.title = title
    note.content = content

    tags = []
    for tag_name in tag_names:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
            db.add(tag)
            db.commit()
            db.refresh(tag)
        tags.append(tag)
    note.tags = tags

    db.commit()
    db.refresh(note)
    return note

def delete_note(db: Session, note_id: int) -> bool:
    note = get_note(db, note_id)
    if not note:
        return False
    db.delete(note)
    db.commit()
    return True

# --- Tag CRUD ---
def get_tags(db: Session) -> List[Tag]:
    return db.query(Tag).all()
