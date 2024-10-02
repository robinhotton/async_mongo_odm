from beanie import Document, Link, BackLink
from typing import List, Optional
from bson import ObjectId
from pydantic import Field


class Matiere(Document):
    nom: str
    professeurs: Optional[List[Link["Professeur"]]] = None
    notes: List[BackLink["Notes"]] = Field(original_field="matiere")

    class Settings:
        collection = "matieres"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "Mathématiques",
                "professeurs": [str(ObjectId())],  # Références aux professeurs
            }
        }
