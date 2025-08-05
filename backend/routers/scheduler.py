from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.services import scheduler_service
from backend.utils.auth import require_role

router = APIRouter(prefix="/scheduler", tags=["scheduler"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/run")
def run_scheduler(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    result = scheduler_service.run_scheduler(db)
    return {"status": "ok", "assignments_created": result}