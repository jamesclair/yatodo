from sqlalchemy.orm import Session
from sqlalchemy import select

from . import models, schemas


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Task).offset(offset).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    status_id = get_status_id_by_name(db=db, status=task.status_name)
    db_task = models.Task(name=task.name, status_id=status_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_status_id_by_name(db: Session, status: str | None) -> int | None:
    return db.scalar(select(models.Status).where(models.Status.name == status)).id
