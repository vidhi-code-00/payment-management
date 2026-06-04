from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.wallet import Wallet
from app.schema.walletschema import WalletCreate

router = APIRouter(
    prefix="/wallet",
    tags=["Wallet"]
)

@router.post("/add-money")
def add_money(data: WalletCreate, db: Session = Depends(get_db)):

    wallet = db.query(Wallet).filter(
        Wallet.user_id == data.user_id
    ).first()

    if wallet:
        wallet.balance += data.amount
    else:
        wallet = Wallet(
            user_id=data.user_id,
            balance=data.amount
        )
        db.add(wallet)

    db.commit()

    return {
        "message": "Money Added Successfully",
        "balance": wallet.balance
    }