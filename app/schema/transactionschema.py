from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    description: str