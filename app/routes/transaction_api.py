from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.payment import Payment
from app.models.refund import Refund
from app.models.transaction_model import Transaction
from app.schema.transactionschema import TransactionCreate

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# ---------------- ADD TRANSACTION ----------------
@router.post("/")
def add_transaction(
    data: TransactionCreate,
    db: Session = Depends(get_db)
):

    transaction = Transaction(
        description=data.description,
        amount=data.amount
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return {
        "message": "Transaction created",
        "data": transaction
    }


# ---------------- GET ALL ----------------
@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()


# ---------------- DELETE ----------------
@router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):

    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted"}


# ---------------- HISTORY ----------------
@router.get("/history/{user_id}")
def transaction_history(
    user_id: int,
    db: Session = Depends(get_db)
):

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