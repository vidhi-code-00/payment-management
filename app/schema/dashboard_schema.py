from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_users: int
    total_transactions: int
    total_amount: int