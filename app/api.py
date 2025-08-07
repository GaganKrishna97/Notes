from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from models import NoteCreate, NoteRead
from service import NoteService

router = APIRouter(prefix="/notes", tags=["notes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=NoteRead)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    try:
        return NoteService.create_note(db, note)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@router.get("/", response_model=List[NoteRead])
def list_notes(db: Session = Depends(get_db)):
    return NoteService.get_notes(db)

@router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: int, db: Session = Depends(get_db)):
    try:
        return NoteService.get_note(db, note_id)
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))

@router.put("/{note_id}", response_model=NoteRead)
def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db)):
    try:
        return NoteService.update_note(db, note_id, note)
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    try:
        NoteService.delete_note(db, note_id)
        return {"msg": "Note deleted"}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
