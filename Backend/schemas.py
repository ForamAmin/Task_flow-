from pydantic import BaseModel , Field , computed_field , field_validator
from typing import List,Annotated , Optional
from datetime import date , datetime
from enum import Enum
class Priority(str , Enum):
        high = 'High'
        medium = 'Medium'
        low = 'Low'
class Status(str , Enum):
     todo = 'To-do'
     in_progress = 'in_progress'
     completed = 'Completed'
     cancelled = 'Cancelled'

class task(BaseModel):
    taskId : Annotated[int , Field(... , description="Give ID of task from 1 to any number" , examples=[1] , gt=0 , title= "ID of task")]
    taskName : Annotated[str , Field(... , description="Name of the task " , examples=['Assignment 1'] , title= "Name of task")]
    priority : Annotated[Priority , Field(..., description="Choose from high , medium , low  " , title="Priority of the task ")]
    duedate : Annotated[date , Field(..., description="Due date ")]
    remarks: Annotated[Optional[str], Field(None , description="Any note/remark for the task")]
    taskStatus : Annotated[Status , Field(... , description="Choose from : to-do , in_progress , completed , cancelled")]

    @field_validator('duedate')
    #Whatever the validator returns becomes the final value stored in the model.
    @classmethod
    def is_valide(cls , v):
        if v<date.today():
            raise ValueError("Due date cannot be in the past ")
        return v
    
    @computed_field
    @property
    def time_remaining(self) -> int:
         due = self.duedate
         today = date.today()
         delta = due - today 
         days_left = delta.days
         return max(days_left , 0)
    
    @computed_field
    @property
    def priority_level(self) -> int:
         mapping = {
         Priority.high: 3,
         Priority.medium: 2,
         Priority.low: 1 }
         level = mapping[self.priority]   
         return level
                
    @computed_field
    @property
    def is_overdue(self) -> bool:
         return self.duedate < date.today()
