from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "secret"
ALGORITHM = "HS256"

pwd = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    return pwd.hash(password)

def verify_password(plain, hashed):
    return pwd.verify(plain, hashed)

def create_token(data: dict):

    data["exp"] = datetime.now(timezone.utc) + timedelta(minutes=30)

    return jwt.encode(
         data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )