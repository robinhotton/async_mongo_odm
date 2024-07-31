from datetime import datetime
from beanie import Document

class Trimestre(Document):
    idtrimestre: int
    nom: str
    date: datetime

    class Settings:
        collection = "trimestres"

    class Config:
        schema_extra = {
            "example": {
                "idtrimestre": 1,
                "nom": "TRIM01",
                "date": "2023-12-01T09:08:03"
            }
        }
