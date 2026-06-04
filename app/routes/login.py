from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schema.userschema import UserLogin
from app.core.security import verify_password, create_token

router = APIRouter()


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    check_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not check_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid Email"
        )

    if not verify_password(
        user.password,
        check_user.password
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid Password"
        )

    token = create_token({
        "user_id": check_user.id,
        "email": check_user.email
    })

    return {
        "message": "Login Successful",
        "access_token": token
    }