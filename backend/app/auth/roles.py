# Different roles definition
from fastapi import HTTPException

ADMIN = "admin"
AGENT_OPERATOR = "agent_operator"
VIEWER = "viewer"

def require_role(user, allowed_roles):

    if user["role"] not in allowed_roles:

        raise HTTPException(
                status_code=403,
                detail="Permission denied."
                )