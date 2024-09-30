from beanie import Document
from typing import Optional
from bson import ObjectId
from pydantic import Field


class Classe(Document):
    nom: str
    prof: Optional[str] = Field(None, alias="prof_id")

    class Settings:
        collection = "classes"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "CP",
                "prof_id": str(ObjectId())
            }
        }