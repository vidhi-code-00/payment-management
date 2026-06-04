from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.payment import Payment
from app.models.refund import Refund

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.get("/{user_id}")
def transaction_history(user_id: int, db: Session = Depends(get_db)):

    payments = db.query(Payment).filter(
        Payment.user_id == user_id
    ).all()

    refunds = db.query(Refund).filter(
        Refund.user_id == user_id
    ).all()

    return {
        "user_id": user_id,
        "payments": payments,
        "refunds": refunds
    }