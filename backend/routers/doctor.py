from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.doctor import Doctor, DoctorCreate
from backend.database import SessionLocal
from backend.services import doctor_service
from backend.utils.auth import get_current_user, require_role

router = APIRouter(prefix="/doctors", tags=["doctors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#@router.get("/", response_model=List[Doctor])
#def list_doctors(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
#    print("=== DEBUG: list_doctors endpoint called ===")
#    return doctor_service.list_doctors(db)

@router.post("/", response_model=Doctor)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return doctor_service.create_doctor(db, doctor)

@router.get("/get-doctors", response_model=List[Doctor])
def list_doctors(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    print("=== DEBUG: get-doctors endpoint called ===")
    return doctor_service.list_doctors(db)