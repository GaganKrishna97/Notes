import uvicorn
from fastapi import FastAPI
from database import Base, engine
from api import router as notes_router

app = FastAPI()
app.include_router(notes_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
