from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .database import Base


class Status(Base):
    __tablename__ = "status"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    tasks: Mapped[list["Task"]] = relationship(init=False, back_populates="status")


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(1000))
    status_id: Mapped[int] = mapped_column(
        ForeignKey("status.id"), insert_default=1, default=None
    )

    status: Mapped[Status] = relationship(init=False, back_populates="tasks")
