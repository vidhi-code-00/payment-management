from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.refund import Refund
from app.schema.refundschema import RefundCreate

router = APIRouter(
    prefix="/refund",
    tags=["Refund"]
)

@router.post("/request")
def request_refund(refund: RefundCreate, db: Session = Depends(get_db)):

    new_refund = Refund(
        payment_id=refund.payment_id,
        user_id=refund.user_id,
        amount=refund.amount,
        reason=refund.reason,
        status="requested"
    )

    db.add(new_refund)
    db.commit()
    db.refresh(new_refund)

    return {
        "message": "Refund Requested Successfully",
        "refund_id": new_refund.id,
        "status": new_refund.status
    }