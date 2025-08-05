from backend.models.shift import Shift, ShiftRequirement
from backend.schemas.shift import ShiftCreate, ShiftRequirementCreate
from sqlalchemy.orm import Session

def list_shifts(db: Session):
    return db.query(Shift).all()

def create_shift(db: Session, shift: ShiftCreate):
    db_shift = Shift(**shift.dict())
    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)
    return db_shift

def list_shift_requirements(db: Session):
    return db.query(ShiftRequirement).all()

def create_shift_requirement(db: Session, req: ShiftRequirementCreate):
    db_req = ShiftRequirement(**req.dict())
    db.add(db_req)
    db.commit()
    db.refresh(db_req)
    return db_req