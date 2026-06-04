from app.core.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float, DateTime, func
from sqlalchemy.orm import relationship


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    amount = Column(Float, nullable=False)

    payment_method = Column(String(50), nullable=False)

    status = Column(String(50), default="pending")

    transaction_id = Column(
        String(100),
        unique=True,
        nullable=True
    )

    create_date = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    update_date = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    user = relationship("User", backref="payments")