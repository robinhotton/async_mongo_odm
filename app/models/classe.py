from beanie import Document
from typing import Optional

class Classe(Document):
    id: int
    nom: Optional[str]
    prof: int

    class Settings:
        collection = "classes"

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nom": "CP",
                "prof": 1
            }
        }
