import jwt
import datetime
from fastapi import HTTPException

SECRET_KEY = "auth-app"
ALGORITHM = "HS256"

def create_jwt_token(data: dict) -> str:
    expiration = datetime.datetime.now() + datetime.timedelta(hours=1)
    to_encode = data.copy()
    to_encode.update({"exp": expiration})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
