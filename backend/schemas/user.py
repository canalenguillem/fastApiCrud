from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class RoleBase(BaseModel):
    name: str


class Role(RoleBase):
    id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    name: str  # Añadir este campo


class User(UserBase):
    id: int
    name: str
    role: Role

    class Config:
        from_attributes = True


class UserDeleteResponse(BaseModel):
    message: str
