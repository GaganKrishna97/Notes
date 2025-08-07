from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(String(1024), nullable=False)

# Pydantic schemas

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteRead(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
