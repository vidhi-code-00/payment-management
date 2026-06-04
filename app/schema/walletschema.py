from pydantic import BaseModel

class WalletCreate(BaseModel):
    user_id: int
    amount: int