import uvicorn
from fastapi import FastAPI
from database import Base, engine
from api import router

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def on_startup():
    # create all tables
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
