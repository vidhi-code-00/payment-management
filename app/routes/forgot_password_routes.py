from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schema.userschema import ForgotPassword
from app.core.security import pwd

router = APIRouter(
    prefix="/auth",
    tags=["Forgot Password"]
)


@router.post("/forgot-password")
def forgot_password(
    data: ForgotPassword,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Email not found"
        )

    hashed_password = pwd.hash(
        data.new_password
    )

    user.password = hashed_password

    db.commit()
    db.refresh(user)

    return {
        "message": "Password changed successfully"
    }
