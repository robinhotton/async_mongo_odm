from beanie import Document
from pydantic import EmailStr
from typing import List
from app.enum.role_enum import RoleEnum


class User(Document):
    username: str
    email: EmailStr
    hashed_password: str
    roles: List[RoleEnum] = [RoleEnum.ELEVE]

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@example.com",
                "hashed_password": "hashedpassword",
                "roles": ["ELEVE"]
            }
        }