# backend/create_tables.py
from backend.database import engine
from backend.models.base import Base
from backend.models import doctor, role, shift, availability, assignment

Base.metadata.create_all(bind=engine)
print("Tables created!")