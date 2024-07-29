from beanie import Document
from pydantic import Field
from typing import List

class Profile(Document):
    username: str
    residence: str
    current_location: List[float]

    class Settings:
        collection = "profiles"

    class Config:
        schema_extra = {
            "example": {
                "username": "john_doe",
                "residence": "123 Elm St",
                "current_location": [-73.935242, 40.730610]
            }
        }
