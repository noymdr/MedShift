from pydantic import BaseModel
from typing import List, Optional

class DoctorBase(BaseModel):
    name: str
    specialty: Optional[str] = None

class DoctorCreate(DoctorBase):
    role_ids: List[int]

class Doctor(DoctorBase):
    id: int
    roles: List[str]  # This expects strings, but you're returning Role objects

    class Config:
        from_attributes = True