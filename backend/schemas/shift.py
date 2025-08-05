from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time

class ShiftBase(BaseModel):
    date: date
    department: str
    start_time: time
    end_time: time
    shift_type: str

class ShiftCreate(ShiftBase):
    pass

class Shift(ShiftBase):
    id: int
    requirements: Optional[List['ShiftRequirement']] = None

    class Config:
        from_attributes = True  # Changed from orm_mode = True

class ShiftRequirementBase(BaseModel):
    role_id: int
    quantity: int

class ShiftRequirementCreate(ShiftRequirementBase):
    shift_id: int

class ShiftRequirement(ShiftRequirementBase):
    id: int
    shift_id: int

    class Config:
        from_attributes = True  # Changed from orm_mode = True