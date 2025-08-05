from backend.models.role import Role
from sqlalchemy.orm import Session

def list_roles(db: Session):
    return db.query(Role).all()