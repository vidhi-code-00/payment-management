from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import get_db
from app.models.payment import Payment
from app.models.razorpay_model import client


@router.post("/verify-payment")
def verify_payment(data: dict, db: Session = Depends(get_db)):

    try:
        # 1. VERIFY SIGNATURE
        client.utility.verify_payment_signature({
            "razorpay_order_id": data["razorpay_order_id"],
            "razorpay_payment_id": data["razorpay_payment_id"],
            "razorpay_signature": data["razorpay_signature"]
        })

        # 2. SAVE TO DATABASE
        new_payment = Payment(
            user_id=data["user_id"],
            amount=data["amount"],
            payment_method="razorpay",
            status="success",
            transaction_id=data["razorpay_payment_id"]
        )

        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)

        return {
            "success": True,
            "message": "Payment Verified & Saved",
            "payment_id": new_payment.id
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Payment verification failed: {str(e)}"
        )