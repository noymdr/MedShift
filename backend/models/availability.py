from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Availability(Base):
    __tablename__ = 'availabilities'
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    date = Column(Date, nullable=False)
    reason = Column(String, nullable=True)

    doctor = relationship('Doctor')