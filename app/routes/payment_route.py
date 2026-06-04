from fastapi import APIRouter

router = APIRouter(
    prefix="/payment",
    tags=["Payment"]
)


@router.post("/pay")
def make_payment():

    return {
        "message": "Payment Successful"
    }