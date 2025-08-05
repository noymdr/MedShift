from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.shift import Shift, ShiftCreate, ShiftRequirement, ShiftRequirementCreate
from backend.database import SessionLocal
from backend.services import shift_service
from backend.utils.auth import require_role

router = APIRouter(prefix="/shifts", tags=["shifts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Shift])
def list_shifts(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return shift_service.list_shifts(db)

@router.post("/", response_model=Shift)
def create_shift(shift: ShiftCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return shift_service.create_shift(db, shift)

@router.get("/requirements", response_model=List[ShiftRequirement])
def list_shift_requirements(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return shift_service.list_shift_requirements(db)

@router.post("/requirements", response_model=ShiftRequirement)
def create_shift_requirement(req: ShiftRequirementCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return shift_service.create_shift_requirement(db, req)