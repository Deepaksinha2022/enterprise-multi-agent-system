from fastapi import FastAPI

from app.auth.middleware import get_current_user
from fastapi import Depends

from app.auth.roles import (
    require_role,
    ADMIN,
    AGENT_OPERATOR
)

# WHAT: Runs code when app starts and stops.
# WHY: Initialize resources such as DB, Redis, agents.

from contextlib import asynccontextmanager

# What: Imports asynccontextmanager.
# Why: Helps create startup and shutdown logic for FastAPI.

@asynccontextmanager

# What: Lifespan function.
# Why: FastAPI calls it when the application starts and stops.

async def lifespan(app):
    print("Application Starting...")
    yield
    print("Application Stopping...")

app = FastAPI(
    lifespan=lifespan
)
# tells to FastAPI to use the lifespan function for startup and shutdown events.

# Depends is FastAPI's dependency injection mechanism. 
# It automatically executes another function before the 
# route handler and injects its return value into the route.

@app.get("/")
async def root(
    user=Depends(get_current_user)
    ):
    return {
        "message": "MAS Running",
        "user": user
    }

from app.db.database import engine

# checkin if the database is reachable when /health endpoint is
# called. If the database is reachable, it returns a healthy 
# status; otherwise, it returns an unhealthy status.

@app.get("/health")
async def health():

    try:
        async with engine.begin() as conn:
            pass

        return {"status": "healthy"}

    except Exception:
        return {"status": "unhealthy"}

# POST is used when you want to create or trigger something
@app.post("/launch-agent")
async def launch_agent(
    user=Depends(get_current_user)
    ):

    require_role(
        user,
        [ADMIN, AGENT_OPERATOR]
    )

    return {
        "message": "Agent launched successfully."
    }