from fastapi import APIRouter
import razorpay
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

client = razorpay.Client(
    auth=(
        os.getenv("RAZORPAY_KEY_ID"),
        os.getenv("RAZORPAY_KEY_SECRET")
    )
)

@router.post("/create-order")
def create_order(amount: int):

    order_data = {
        "amount": amount * 100,   # paise me
        "currency": "INR",
        "payment_capture": 1
    }

    order = client.order.create(data=order_data)

    return {
    "order_id": order["id"],
    "amount": order["amount"],
    "currency": order["currency"]
}