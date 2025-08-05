from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .association import doctor_roles  # <-- updated import

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    doctors = relationship('Doctor', secondary=doctor_roles, back_populates='roles')