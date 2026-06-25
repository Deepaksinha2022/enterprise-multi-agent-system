# WHAT: Simple script to test PostgreSQL connection.
# WHY: Verify FastAPI can reach the database.

from app.db.database import engine
import asyncio

# asyncio is Python's built-in library 
# for running asynchronous code.

async def test_connection():
    async with engine.begin() as conn:
        print("Database Connected!")

# WHAT: Executes the async function.
# WHY: Python won't run async functions automatically.

asyncio.run(test_connection())