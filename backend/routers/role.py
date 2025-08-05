from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.role import Role
from backend.database import SessionLocal
from backend.services import role_service

router = APIRouter(prefix="/roles", tags=["roles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Role])
def list_roles(db: Session = Depends(get_db)):
    return role_service.list_roles(db)