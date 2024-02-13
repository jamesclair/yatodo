from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import SessionLocal, engine


import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks", response_model=list[schemas.Task])
def get_tasks(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(offset=offset, limit=limit, db=db)
    return tasks


@app.post("/task", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)
