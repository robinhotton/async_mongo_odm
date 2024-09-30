from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TrimestreBaseSchema(BaseModel):
    nom: str
    date: datetime

    class Config:
        from_attributes = True

class CreateTrimestreSchema(TrimestreBaseSchema):
    pass

class UpdateTrimestreSchema(BaseModel):
    nom: Optional[str] = None
    date: Optional[datetime] = None

class TrimestreSchema(TrimestreBaseSchema):
    idtrimestre: str

    class Config:
        json_schema_extra = {
            "example": {
                "idtrimestre": str(ObjectId()),
                "nom": "TRIM01",
                "date": "2023-12-01T09:08:03"
            }
        }
