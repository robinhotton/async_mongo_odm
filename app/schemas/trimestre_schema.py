from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .py_object_id import PyObjectId


class TrimestreBase(BaseModel):
    nom: str
    date: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nom": "TRIM01",
                "date": "2023-12-01T09:08:03"
            }
        }


class TrimestreCreate(TrimestreBase):
    pass


class TrimestreUpdate(BaseModel):
    nom: Optional[str] = None
    date: Optional[datetime] = None


class TrimestreResponse(TrimestreBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed=True,
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "nom": "TRIM01",
                "date": "2023-12-01T09:08:03"
            }
        }