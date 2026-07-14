from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schema.userschema import UserLogin
from app.core.security import verify_password, create_token

router = APIRouter()


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    # 1. USER FIND
    check_user = db.query(User).filter(User.email == user.email).first()

    if not check_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid Email"
        )

    # 2. PASSWORD CHECK (SAFE)
    if not check_user.password:
        raise HTTPException(
            status_code=500,
            detail="Password missing in database"
        )

    try:
        is_valid = verify_password(user.password, check_user.password)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Password verification error: {str(e)}"
        )

    if not is_valid:
        raise HTTPException(
            status_code=400,
            detail="Invalid Password"
        )

    # 3. TOKEN GENERATION (SAFE)
    try:
        token = create_token({
            "user_id": check_user.id,
            "email": check_user.email
        })
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Token generation error: {str(e)}"
        )

    # 4. RESPONSE
    return {
        "message": "Login Successful",
        "access_token": token
    }