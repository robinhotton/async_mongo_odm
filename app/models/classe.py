from beanie import Document, Link, BackLink
from typing import Optional, List
from bson import ObjectId
from pydantic import Field


class Classe(Document):
    nom: str
    prof: Optional[Link["Professeur"]] = None
    eleves: BackLink["Eleve"] = Field(original_field="classe")

    class Settings:
        collection = "classes"
    
    class Config:
        json_schema_extra = {
            "example": {
                "nom": "CP",
                "prof": str(ObjectId())
            }
        }
