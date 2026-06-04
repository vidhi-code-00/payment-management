from pydantic import BaseModel
from typing import Optional


class RefundRequest(BaseModel):
    payment_id: int
    amount: int
    reason: Optional[str] = None


class RefundResponse(BaseModel):
    id: int
    payment_id: int
    amount: int
    status: str
    reason: Optional[str]

    class Config:
        from_attributes = True