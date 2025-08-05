from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .association import doctor_roles

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=True)
    # Add more fields as needed

    roles = relationship('Role', secondary=doctor_roles, back_populates='doctors')