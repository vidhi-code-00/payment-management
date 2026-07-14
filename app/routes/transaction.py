from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import razorpay

from app.core.database import get_db
from app.models.transaction_model import Transaction
from app.schema.transactionschema import TransactionCreate

# Razorpay Client
client = razorpay.Client(
    auth=(
        "YOUR_KEY_ID",
        "YOUR_KEY_SECRET"
    )
)

router = APIRouter(
    prefix="/api/transaction"
)

@router.get("/test")
def test():
    return {
        "message": "Transaction route working"
    }

@router.post("/add")
def add_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    new_transaction = Transaction(
        amount=transaction.amount,
        description=transaction.description
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return {
        "message": "Transaction Added"
    }


@router.get("/all")
def get_transactions(
    db: Session = Depends(get_db)
):
    transactions = db.query(Transaction).all()

    return transactions


@router.post("/create-order")
def create_order():
    amount = 500

    order = client.order.create({
        "amount": amount * 100,  # amount in paise
        "currency": "INR",
        "payment_capture": 1
    })

    return order