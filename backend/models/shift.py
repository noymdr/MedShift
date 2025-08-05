from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Shift(Base):
    __tablename__ = 'shifts'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    department = Column(String, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    shift_type = Column(String, nullable=False)  # e.g., "night"

    requirements = relationship('ShiftRequirement', back_populates='shift')
    assignments = relationship('Assignment', back_populates='shift')

class ShiftRequirement(Base):
    __tablename__ = 'shift_requirements'
    id = Column(Integer, primary_key=True, index=True)
    shift_id = Column(Integer, ForeignKey('shifts.id'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    shift = relationship('Shift', back_populates='requirements')
    role = relationship('Role')