from fastapi import FastAPI

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

@app.get("/")
async def root():
    return {"message": "MAS Running"}

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