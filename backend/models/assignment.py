from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True, index=True)
    shift_id = Column(Integer, ForeignKey('shifts.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    is_auto_assigned = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    shift = relationship('Shift', back_populates='assignments')
    doctor = relationship('Doctor')
    role = relationship('Role')