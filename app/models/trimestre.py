from datetime import datetime
from beanie import Document

class Trimestre(Document):
    nom: str
    date: datetime

    class Settings:
        collection = "trimestres"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "TRIM01",
                "date": "2023-12-01T09:08:03"
            }
        }