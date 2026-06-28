from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.auth.jwt_handler import verify_token

security = HTTPBearer()

# HTTPBearer() automatically extracts:
# Authorization: Bearer <JWT>
# from the request header.

# HTTPAuthorizationCredentials is a FastAPI class that holds 
# the credentials extracted from the Authorization header.

# FastAPI (HTTPBearer) converts it into an object:

# HTTPAuthorizationCredentials(
#     scheme="Bearer",
#     credentials="eyJhbGciOiJIUzI1NiIs..."
# )

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    payload = verify_token(
        credentials.credentials
    )

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload