from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import BaseModel

router = APIRouter()

# ===============================
# CONFIG
# ===============================
SECRET_KEY = "hackathon_secret_key"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# In-memory database (hackathon safe)
users_db = {}

# ===============================
# REQUEST MODEL (IMPORTANT FIX)
# ===============================
class AuthRequest(BaseModel):
    username: str
    password: str


# ===============================
# TOKEN CREATION
# ===============================
def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ===============================
# GET CURRENT USER (JWT VERIFY)
# ===============================
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# ===============================
# REGISTER
# ===============================
@router.post("/register")
def register(data: AuthRequest):
    username = data.username
    password = data.password

    if username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    users_db[username] = pwd_context.hash(password)
    return {"message": "User registered successfully"}


# ===============================
# LOGIN
# ===============================
@router.post("/login")
def login(data: AuthRequest):
    username = data.username
    password = data.password

    if username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(password, users_db[username]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(username)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
