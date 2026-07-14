from pydantic import BaseModel, EmailStr

class ForgotPassword(BaseModel):
    email: EmailStr
    new_password: str