from datetime import datetime
from beanie import Document
from bson import ObjectId
from pydantic import Field
from typing import Optional

class Notes(Document):
    date_saisie: datetime
    eleve: Optional[ObjectId] = Field(None, alias="eleve_id")  # Référence à l'ID de l'élève
    classe: Optional[ObjectId] = Field(None, alias="classe_id")  # Référence à l'ID de la classe
    matiere: Optional[ObjectId] = Field(None, alias="matiere_id")  # Référence à l'ID de la matière
    prof: Optional[ObjectId] = Field(None, alias="prof_id")  # Référence à l'ID du professeur
    trimestre: Optional[ObjectId] = Field(None, alias="trimestre_id")  # Référence à l'ID du trimestre
    note: int
    avis: str
    avancement: float

    class Settings:
        collection = "notes"

    class Config:
        schema_extra = {
            "example": {
                "date_saisie": "2019-10-15T08:07:03",
                "eleve_id": "60d21b4667d0d8992e610c85",
                "classe_id": "60d21b4667d0d8992e610c85",
                "matiere_id": "60d21b4667d0d8992e610c85",
                "prof_id": "60d21b4667d0d8992e610c85",
                "trimestre_id": "60d21b4667d0d8992e610c85",
                "note": 12,
                "avis": "Travail à approfondir",
                "avancement": 0.5
            }
        }
