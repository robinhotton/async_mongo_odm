from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.enum.role_enum import RoleEnum

class UserCreateSchema(BaseModel):
    username: str
    password: str  # plain text password
    email: EmailStr
    roles: List[RoleEnum] = [RoleEnum.ELEVE]

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@example.com",
                "password": "password",
                "roles": ["ELEVE"]
            }
        }
        
class UserResponseSchema(BaseModel):
    id: str
    username: str
    email: str
    roles: List[RoleEnum]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "605c72ef3f1b2b001f2e8b7c",
                "username": "johndoe",
                "email": "johndoe@example.com",
                "roles": ["ADMIN"]
            }
        }

class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str

class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    roles: Optional[List[RoleEnum]] = None

class UserSchema(BaseModel):
    id: str
    username: str
    email: EmailStr
    roles: List[RoleEnum]
