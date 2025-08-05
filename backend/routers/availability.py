from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.availability import Availability, AvailabilityCreate
from backend.database import SessionLocal
from backend.services import availability_service
from backend.utils.auth import get_current_user, require_role

router = APIRouter(prefix="/availability", tags=["availability"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/me", response_model=List[Availability])
def get_my_availability(db: Session = Depends(get_db), user=Depends(require_role("doctor"))):
    return availability_service.get_doctor_availability(db, user["sub"])

@router.post("/me", response_model=Availability)
def add_unavailability(avail: AvailabilityCreate, db: Session = Depends(get_db), user=Depends(require_role("doctor"))):
    return availability_service.add_unavailability(db, user["sub"], avail)