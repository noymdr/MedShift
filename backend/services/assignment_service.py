from backend.models.assignment import Assignment
from sqlalchemy.orm import Session

def list_assignments(db: Session):
    return db.query(Assignment).all()