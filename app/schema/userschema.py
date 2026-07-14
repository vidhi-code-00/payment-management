from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=6, max_length=72)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class ForgotPassword(BaseModel):
    email: EmailStr
    new_password: str