from pydantic import BaseModel


class PaymentCreate(BaseModel):
    amount: float
    payment_method: str


class PaymentResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    payment_method: str
    status: str
    transaction_id: str | None

    class Config:
        from_attributes = True