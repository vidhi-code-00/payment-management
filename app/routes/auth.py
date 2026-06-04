from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.schema.userschema import UserCreate

from app.core.database import get_db
from app.models.user import User

router = APIRouter(
    prefix="/api/auth"
)

pwd = CryptContext(schemes=["bcrypt"],deprecated="auto")


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    check_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if check_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=pwd.hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered"
    }