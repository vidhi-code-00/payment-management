from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    # Transaction Title
    description = Column(String(255), nullable=False)

    # Transaction Amount
    amount = Column(Float, nullable=False)