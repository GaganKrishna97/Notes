from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database import SessionLocal
from service import UserService, NoteService, TagService

from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Schemas

class UserCreate(BaseModel):
    username: str

class UserRead(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class NoteCreate(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = []

class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    tags: List[str]

    class Config:
        orm_mode = True

class TagRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# User endpoints

@router.post("/users/", response_model=UserRead)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    try:
        user = UserService.create_user(db, user_in.username)
        return user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = UserService.get_user(db, user_id)
        return user
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))

# Notes endpoints

@router.post("/users/{user_id}/notes/", response_model=NoteRead)
def create_note(user_id: int, note: NoteCreate, db: Session = Depends(get_db)):
    try:
        created_note = NoteService.create_note(db, user_id, note.title, note.content, note.tags)
        tags = [tag.name for tag in created_note.tags]
        return NoteRead(
            id=created_note.id,
            title=created_note.title,
            content=created_note.content,
            owner_id=created_note.owner_id,
            tags=tags
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@router.get("/users/{user_id}/notes/", response_model=List[NoteRead])
def get_notes(user_id: int, db: Session = Depends(get_db)):
    notes = NoteService.get_notes(db, user_id)
    result = []
    for note in notes:
        tags = [tag.name for tag in note.tags]
        result.append(
            NoteRead(
                id=note.id,
                title=note.title,
                content=note.content,
                owner_id=note.owner_id,
                tags=tags
            )
        )
    return result

@router.get("/notes/{note_id}", response_model=NoteRead)
def get_note(note_id: int, db: Session = Depends(get_db)):
    try:
        note = NoteService.get_note(db, note_id)
        tags = [tag.name for tag in note.tags]
        return NoteRead(
            id=note.id,
            title=note.title,
            content=note.content,
            owner_id=note.owner_id,
            tags=tags
        )
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))

@router.put("/notes/{note_id}", response_model=NoteRead)
def update_note(note_id: int, note_in: NoteCreate, db: Session = Depends(get_db)):
    try:
        note = NoteService.update_note(db, note_id, note_in.title, note_in.content, note_in.tags)
        tags = [tag.name for tag in note.tags]
        return NoteRead(
            id=note.id,
            title=note.title,
            content=note.content,
            owner_id=note.owner_id,
            tags=tags
        )
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))

@router.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    try:
        NoteService.delete_note(db, note_id)
        return {"msg": "Note deleted"}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))

# Tags endpoint

@router.get("/tags/", response_model=List[TagRead])
def list_tags(db: Session = Depends(get_db)):
    tags = TagService.get_tags(db)
    return tags
