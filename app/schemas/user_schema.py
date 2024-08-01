from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.enum.role_enum import RoleEnum

class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str  # plain text password
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

class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    roles: Optional[List[RoleEnum]] = None

class UserSchema(BaseModel):
    id: str
    username: str
    email: EmailStr
    roles: List[RoleEnum]
