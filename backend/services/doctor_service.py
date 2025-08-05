from backend.models.doctor import Doctor, doctor_roles
from backend.models.role import Role
from backend.schemas.doctor import DoctorCreate
from sqlalchemy.orm import Session

def list_doctors(db: Session):
    doctors = db.query(Doctor).all()
    
    # Convert to response format
    result = []
    for doctor in doctors:
        doctor_dict = {
            "id": doctor.id,
            "name": doctor.name,
            "specialty": doctor.specialty,
            "roles": [role.name for role in doctor.roles]  # Convert Role objects to strings
        }
        result.append(doctor_dict)
    
    return result

def create_doctor(db: Session, doctor: DoctorCreate):
    db_doctor = Doctor(name=doctor.name, specialty=doctor.specialty)
    roles = db.query(Role).filter(Role.id.in_(doctor.role_ids)).all()
    db_doctor.roles = roles
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor