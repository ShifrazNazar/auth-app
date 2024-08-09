from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlite3 import connect
import jwt
import datetime
from typing import Optional

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
DB_PATH = "/Users/m2air16-256/Developer/Personal/auth-app.db"

def get_db_connection():
    conn = connect(DB_PATH)
    return conn

class User(BaseModel):
    username: str
    password: str

SECRET_KEY = "auth-app"
ALGORITHM = "HS256"

def create_jwt_token(data: dict):
    expiration = datetime.datetime.now() + datetime.timedelta(hours=1)
    to_encode = data.copy()
    to_encode.update({"exp": expiration})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/login")
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

@app.get("/validate_token")
async def validate_token(request: Request, token: str):
    payload = verify_jwt_token(token)
    return {"message": "Token is valid", "user": payload["sub"]}

@app.get("/")
async def root():
    return {"message": "Welcome to the authentication API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
