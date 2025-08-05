from backend.models.availability import Availability
from backend.schemas.availability import AvailabilityCreate
from sqlalchemy.orm import Session

def get_doctor_availability(db: Session, doctor_id: int):
    return db.query(Availability).filter(Availability.doctor_id == doctor_id).all()

def add_unavailability(db: Session, doctor_id: int, avail: AvailabilityCreate):
    db_avail = Availability(doctor_id=doctor_id, date=avail.date, reason=avail.reason)
    db.add(db_avail)
    db.commit()
    db.refresh(db_avail)
    return db_avail