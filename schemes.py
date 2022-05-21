from pydantic import BaseModel

class RegisterInfo(BaseModel):
    username: str
    email: str
    password: str
    businessType: int

class LoginInfo(BaseModel):
    username: str
    password: str

