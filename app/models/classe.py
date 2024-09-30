from beanie import Document
from typing import Optional
from bson import ObjectId
from pydantic import Field

class Classe(Document):
    nom: Optional[str] = None
    prof: Optional[ObjectId] = Field(None, alias="prof_id")  # Référence à l'ID du professeur

    class Settings:
        collection = "classes"

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "nom": "CP",
                "prof_id": "60d21b4667d0d8992e610c85"  # Exemple d'ObjectId d'un professeur
            }
        }
