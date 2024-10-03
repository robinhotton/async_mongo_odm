from beanie import Document, BackLink
from typing import List
from pydantic import Field
    

class Matiere(Document):
    nom: str
    notes: BackLink["Note"] = Field(original_field="matiere")

    class Settings:
        collection = "matieres"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "Mathématiques"
            }
        }