from app.core.database import Base
from sqlalchemy import Column,Integer,ForeignKey,String,DateTime,func
from sqlalchemy.orm import relationship

class UserToken(Base):
    __tablename__ = "user_token"
    id= Column(Integer,primary_key=True, index= True)
    user_id= Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable = False, index=True)
    jwt_token= Column(String(1000),unique=True,nullable=False)
    expires_at=Column(DateTime(timezone=True),nullable=False)
    create_date=Column(DateTime(timezone=True),server_default=func.now(), nullable=False)
    update_date=Column(DateTime(timezone=True),server_default=func.now(), nullable=False,onupdate=func.now())
    user=relationship("User",backref="tokens")
