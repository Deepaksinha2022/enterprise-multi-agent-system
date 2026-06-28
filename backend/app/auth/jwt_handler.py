import jwt
from datetime import datetime, timedelta

with open("private.pem", "r") as f:
    PRIVATE_KEY = f.read()

with open("public.pem", "r") as f:
    PUBLIC_KEY = f.read()


def create_token(username: str, role: str):

    payload = {
        "username": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }

    return jwt.encode(
    payload,
    PRIVATE_KEY,
    algorithm="RS256"
    )


token = create_token(
    "deepak",
    "viewer"
    )

print(token)

from jwt.exceptions import InvalidTokenError

def verify_token(token: str):

    try:

        return jwt.decode(
            token,
            PUBLIC_KEY,
            algorithms=["RS256"]
        )

    except InvalidTokenError:

        return None

decoded = verify_token(token)

print(decoded)