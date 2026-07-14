from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone

from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt

from app.core.database import get_db
from app.models.user import User
from app.models.user_token import UserToken

router = APIRouter()

# ---------------- CONFIG ----------------
SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ---------------- REQUEST MODELS ----------------
class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


# ---------------- TOKEN ----------------
def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(hours=1)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ---------------- REGISTER ----------------
@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):

    # check user exists
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    # hash password
    hashed_password = pwd_context.hash(data.password)

    new_user = User(
        name=data.name,
        email=data.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


# ---------------- LOGIN ----------------
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({
        "user_id": user.id,
        "email": user.email
    })

    # save token
    db_token = UserToken(
        user_id=user.id,
        jwt_token=token,
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1)
    )

    db.add(db_token)
    db.commit()

    return {
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }