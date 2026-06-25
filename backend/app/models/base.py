# WHAT: Base class for all database tables.
# WHY: Every model inherits from this.

from sqlalchemy.orm import DeclarativeBase

# Base acts as the common parent for
# all SQLAlchemy models and stores metadata about all tables.
class Base(DeclarativeBase):
    pass