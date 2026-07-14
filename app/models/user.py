from app.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, index=True, nullable=False)

    password = Column(String(255), nullable=False)

    user_type = Column(String(100), nullable=False, default="USER")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )