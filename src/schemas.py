from __future__ import annotations  # top of file required

from pydantic import BaseModel


class StatusBase(BaseModel):
    name: str | None = None


class StatusCreate(StatusBase):
    pass


class Status(StatusBase):
    id: int
    tasks: list[Task] = []

    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    name: str
    status_name: str | None = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True
