from datetime import datetime
from beanie import Document
from pydantic import Field
from typing import Optional
from bson import ObjectId


class Notes(Document):
    date_saisie: datetime
    eleve: Optional[str] = Field(None, alias="eleve_id")
    classe: Optional[str] = Field(None, alias="classe_id")
    matiere: Optional[str] = Field(None, alias="matiere_id")
    prof: Optional[str] = Field(None, alias="prof_id")
    trimestre: Optional[str] = Field(None, alias="trimestre_id")
    note: int
    avis: str
    avancement: float

    class Settings:
        collection = "notes"

    class Config:
        json_schema_extra = {
            "example": {
                "date_saisie": "2019-10-15T08:07:03",
                "eleve_id": str(ObjectId()),
                "classe_id": str(ObjectId()),
                "matiere_id": str(ObjectId()),
                "prof_id": str(ObjectId()),
                "trimestre_id": str(ObjectId()),
                "note": 12,
                "avis": "Travail à approfondir",
                "avancement": 0.5
            }
        }