from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

doctor_roles = Table(
    'doctor_roles', Base.metadata,
    Column('doctor_id', Integer, ForeignKey('doctors.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
) 