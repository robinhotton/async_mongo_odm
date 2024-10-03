from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from ..enums import RoleEnum
from .py_object_id import PyObjectId


class UserBase(BaseModel):
    username: str
    email: EmailStr
    roles: List[RoleEnum] = [RoleEnum.ELEVE]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@example.com",
                "roles": [RoleEnum.ELEVE]
            }
        }


class UserCreate(UserBase):
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@example.com",
                "password": "password",
                "roles": [RoleEnum.ELEVE]
            }
        }


class UserUpdate(UserBase):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    roles: Optional[List[RoleEnum]] = None


class UserResponse(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed=True,
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "username": "johndoe",
                "email": "johndoe@example.com",
                "roles": [RoleEnum.ADMIN]
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str