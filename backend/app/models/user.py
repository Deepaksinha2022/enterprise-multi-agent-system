# WHAT: First database table.
# WHY: Stores user information.

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):

    # What: Table name in PostgreSQL.
    # Why: SQLAlchemy creates:
    __tablename__ = "users"

    # What: id column stores integers.
    # Why: Type hint for SQLAlchemy + Python.

    id: Mapped[int] = mapped_column(primary_key=True)

    # What: Defines a database column.
    # Why: Makes id the primary key.

    username: Mapped[str] = mapped_column(String(100))

    # What: Username column stores text.
    # Why: Every user has a username.

    email: Mapped[str] = mapped_column(String(255))

    # What: Email column stores text.
    # Why: User email.