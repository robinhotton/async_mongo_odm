from beanie import Document
from pydantic import EmailStr
from typing import List
from datetime import datetime
from ..enums import RoleEnum


class User(Document):
    username: str
    email: EmailStr
    hashed_password: str
    roles: List[RoleEnum] = [RoleEnum.ELEVE]
    date_creation: datetime = datetime.utcnow()
    derniere_connexion: datetime = None
    active: bool = True

    class Settings:
        collection = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@example.com",
                "hashed_password": "hashedpassword",
                "roles": [RoleEnum.ELEVE],
                "date_creation": "2023-10-01T10:00:00",
                "derniere_connexion": "2023-10-10T15:30:00",
                "active": True
            }
        }
