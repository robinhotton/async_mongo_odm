from beanie import Document, Link
from typing import Optional
from datetime import datetime
from bson import ObjectId


class Notes(Document):
    date_saisie: datetime
    eleve: Optional[Link["Eleve"]] = None
    classe: Optional[Link["Classe"]] = None
    matiere: Optional[Link["Matiere"]] = None
    prof: Optional[Link["Professeur"]] = None
    trimestre: Optional[Link["Trimestre"]] = None
    note: int
    avis: str
    avancement: float

    class Settings:
        collection = "notes"

    class Config:
        json_schema_extra = {
            "example": {
                "date_saisie": "2019-10-15T08:07:03",
                "eleve": str(ObjectId()),
                "classe": str(ObjectId()),
                "matiere": str(ObjectId()),
                "prof": str(ObjectId()),
                "trimestre": str(ObjectId()),
                "note": 12,
                "avis": "Travail à approfondir",
                "avancement": 0.5
            }
        }
