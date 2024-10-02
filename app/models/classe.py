from beanie import Document, Link
from bson import ObjectId
from typing import Optional
from .professeur import Professeur


class Classe(Document):
    nom: str
    prof: Optional[Link[Professeur]] = None  # Lien direct vers le professeur responsable

    class Settings:
        collection = "classes"

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nom": "CP",
                "prof": str(ObjectId())  # Référence au professeur responsable
            }
        }