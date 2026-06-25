# WHAT: Validates incoming user data.
# WHY: Ensures API receives correct fields and types.

from pydantic import BaseModel

    # Pydantic
    # A Python library for:
    # Data validation
    # Data parsing
    # Data serialization

    # Pydantic is a data validation library used by FastAPI.
    # A Pydantic model defines the structure and 
    # types of incoming or outgoing data and
    # automatically validates it.

class UserCreate(BaseModel): # to validate data when creating a new user
    username: str
    email: str