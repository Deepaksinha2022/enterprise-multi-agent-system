# WHAT: Creates all database tables.
# WHY: Converts SQLAlchemy models into actual PostgreSQL tables.

import asyncio

from app.db.database import engine
from app.models.base import Base
from app.models.user import User


async def create_tables():
    async with engine.begin() as conn:

        # What: Finds all models inheriting from Base.
        # Why: Creates their tables in PostgreSQL.
        # A model is a Python class that represents
        # a database table.
        
        await conn.run_sync(Base.metadata.create_all)

        # metadata → Registry/catalog of all models and table definitions.
        # create_all() → Creates tables in the database from models.
        # run_sync() → Executes synchronous SQLAlchemy operations inside an async connection
        # Base.metadata.create_all() scans all models inheriting 
        # from Base and creates the corresponding tables 
        # in the database if they don't already exist.
        
asyncio.run(create_tables())