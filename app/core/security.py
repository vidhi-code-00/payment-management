from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 🔐 Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)


# 🔍 Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# 🔑 Create JWT Token
def create_token(data: dict):
    payload = data.copy()

    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=30)

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)