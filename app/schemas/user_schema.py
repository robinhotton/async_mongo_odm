from bson import ObjectId
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from ..enums import RoleEnum


class UserBaseSchema(BaseModel):
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


class UserCreateSchema(UserBaseSchema):
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


class UserUpdateSchema(UserBaseSchema):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    roles: Optional[List[RoleEnum]] = None

    
class UserResponseSchema(UserBaseSchema):
    _id: str

    class Config:
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "username": "johndoe",
                "email": "johndoe@example.com",
                "roles": [RoleEnum.ADMIN]
            }
        }
    
    
class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str