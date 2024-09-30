from beanie import Document
from bson import ObjectId
from pydantic import Field

class Matiere(Document):
    nom: str

    class Settings:
        collection = "matieres"

    class Config:
        schema_extra = {
            "example": {
                "nom": "LECTURE-CP"
            }
        }
