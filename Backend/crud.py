# crud.py
from sqlalchemy.orm import Session
from .models import TaskModel
from .schemas import task

def create_task(db: Session, task: task):
    db_task = TaskModel(
        taskId=task.taskId,
        taskName=task.taskName,
        priority=task.priority,
        duedate=task.duedate,
        remarks=task.remarks,
        taskStatus=task.taskStatus
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
