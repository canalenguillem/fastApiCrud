# schemas/user.py
from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    role: Role  # Relación con el rol

    class Config:
        orm_mode = True
