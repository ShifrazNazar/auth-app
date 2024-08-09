from fastapi import APIRouter, HTTPException, Request
from app.models import User
from app.auth.jwt_handler import create_jwt_token, verify_jwt_token
from app.database import get_db_connection

router = APIRouter()

@router.post("/login")
async def login(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user.username, user.password))
    row = cursor.fetchone()
    conn.close()

    if row:
        token = create_jwt_token({"sub": user.username})
        return {"message": "Login successful", "token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@router.get("/validate_token")
async def validate_token(request: Request, token: str):
    payload = verify_jwt_token(token)
    return {"message": "Token is valid", "user": payload["sub"]}
