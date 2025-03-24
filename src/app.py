"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Join the school basketball team and compete in local tournaments",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["alex@mergington.edu", "jessica@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Train and play soccer matches with the school team",
        "schedule": "Mondays, Wednesdays, Fridays, 3:30 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various art forms and create your own masterpieces",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Drama Club": {
        "description": "Participate in theater productions and improve your acting skills",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 12,
        "participants": ["lucas@mergington.edu", "isabella@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for math competitions",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 15,
        "participants": ["ethan@mergington.edu", "sophia@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["oliver@mergington.edu", "emma@mergington.edu"]
    }
}