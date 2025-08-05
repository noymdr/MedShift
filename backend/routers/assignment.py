from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.assignment import Assignment, AssignmentCreate
from backend.database import SessionLocal
from backend.services import assignment_service
from backend.utils.auth import require_role

router = APIRouter(prefix="/assignments", tags=["assignments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Assignment])
def list_assignments(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return assignment_service.list_assignments(db)