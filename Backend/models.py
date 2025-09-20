# models.py
from sqlalchemy import Column, Integer, String, Date, Enum
from .database import Base
import enum


# 1. Priority Enum (for DB storage)
class PriorityEnum(str, enum.Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"


# 2. Status Enum
class StatusEnum(str, enum.Enum):
    Todo = "To-do"
    InProgress = "In-progress"
    Completed = "Completed"
    Cancelled = "Cancelled"


# 3. Task Model (represents "tasks" table in DB)
class TaskModel(Base):
    __tablename__ = "tasks"  # name of table in DB

    taskId = Column(Integer, primary_key=True, index=True)
    taskName = Column(String, nullable=False)
    priority = Column(Enum(PriorityEnum), nullable=False)
    duedate = Column(Date, nullable=False)
    remarks = Column(String, nullable=True)
    taskStatus = Column(Enum(StatusEnum), nullable=False)
