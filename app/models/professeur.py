from datetime import datetime
from beanie import Document
from typing import Optional
from app.enum.sexe_enum import SexeEnum


class Professeur(Document):
    nom: str
    prenom: Optional[str] = None
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Settings:
        collection = "professeurs"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "GERMAIN",
                "prenom": "Christophe",
                "date_naissance": "1971-01-01T23:00:00",
                "adresse": "15 rue du printemps 59000 LILLE",
                "sexe": "HOMME"
            }
        }