import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from backend.routers import doctor, role, availability, shift, assignment, scheduler

app = FastAPI(title="MedShift Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(doctor.router)
app.include_router(role.router)
app.include_router(availability.router)
app.include_router(shift.router)
app.include_router(assignment.router)
app.include_router(scheduler.router)

@app.get("/")
def read_root():
    return {"message": "MedShift Backend API", "docs": "/docs"}