from pydantic import BaseModel
from typing import Optional
from datetime import date

class AvailabilityBase(BaseModel):
    date: date
    reason: Optional[str] = None

class AvailabilityCreate(AvailabilityBase):
    pass

class Availability(AvailabilityBase):
    id: int
    doctor_id: int

    class Config:
        from_attributes = True  # Changed from orm_mode = True