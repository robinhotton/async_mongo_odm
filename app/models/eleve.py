from datetime import datetime
from beanie import Document
from typing import Optional
from app.enum.sexe_enum import SexeEnum
from pydantic import Field
from bson import ObjectId


class Eleve(Document):
    nom: str
    prenom: Optional[str] = None
    classe: Optional[str] = Field(None, alias="classe_id")
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Settings:
        collection = "eleves"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "Durand",
                "prenom": "Marie",
                "classe_id": str(ObjectId()),
                "date_naissance": "2015-01-01T23:00:00",
                "adresse": "15 rue du Lac 75001 Paris",
                "sexe": "FEMME"
            }
        }