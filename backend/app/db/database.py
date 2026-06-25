from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)

DATABASE_URL = (
    "postgresql+asyncpg://postgres:postgres@localhost:5433/enterprise_mas"
)
# DATABASE_URL is the connection string that contains the 
# database location and credentials. engine uses that 
# URL to create and manage actual database connections.
# engine - Manages database connections.
# Creates the database connection manager.

engine = create_async_engine(DATABASE_URL)

# AsyncSession → Used to execute queries.
# inserts, updates, and commits.

# session = actual conversation with database

# async_sessionmaker Factory that creates sessions when needed.

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

