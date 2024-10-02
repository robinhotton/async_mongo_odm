from beanie import Document
from bson import ObjectId
from typing import Optional


class Classe(Document):
    nom: str
    prof_id: Optional[str] = None

    class Settings:
        collection = "classes"

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nom": "CP",
                "prof_id": str(ObjectId())
            }
        }