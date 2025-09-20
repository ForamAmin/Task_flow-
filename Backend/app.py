from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import task
from .database import engine, get_db
from .models import Base, TaskModel
from .crud import create_task

# Create tables at startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health():
    return {"message": "Working !!"}

@app.get("/")
def home():
    return {"message": "Home page "}

@app.post("/create")
def createTask(task: task, db: Session = Depends(get_db)):
    return create_task(db, task)