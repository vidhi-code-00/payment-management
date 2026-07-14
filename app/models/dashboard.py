from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class Dashboard(Base):
    __tablename__ = "dashboard"

    id = Column(Integer, primary_key=True, index=True)

    total_users = Column(Integer, default=0)

    total_transactions = Column(Integer, default=0)

    total_amount = Column(Integer, default=0)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )