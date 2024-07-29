from pydantic import BaseModel, Field
from typing import Optional, List

class ProfileSchema(BaseModel):
    username: str
    residence: str
    current_location: List[float]

    class Config:
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "residence": "123 Elm St",
                "current_location": [-73.935242, 40.730610]
            }
        }

class UpdateProfileSchema(BaseModel):
    username: Optional[str] = None
    residence: Optional[str] = None
    current_location: Optional[List[float]] = None
