from datetime import datetime
from beanie import Document
from typing import Optional
from app.enum.sexe_enum import SexeEnum

class Eleve(Document):
    id: int
    nom: str
    prenom: Optional[str]
    classe: int
    date_naissance: datetime
    adresse: Optional[str]
    sexe: SexeEnum

    class Settings:
        collection = "eleves"

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nom": "Durand",
                "prenom": "Marie",
                "classe": 1,
                "date_naissance": "2015-01-01T23:00:00",
                "adresse": "15 rue du Lac 75001 Paris",
                "sexe": "FEMME"
            }
        }
