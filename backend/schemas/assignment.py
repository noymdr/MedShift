from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AssignmentBase(BaseModel):
    shift_id: int
    doctor_id: int
    role_id: int
    is_auto_assigned: Optional[bool] = True

class AssignmentCreate(AssignmentBase):
    pass

class Assignment(AssignmentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Changed from orm_mode = True