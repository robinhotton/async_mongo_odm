from datetime import datetime
from beanie import Document
from typing import Optional
from app.models.sexe_enum import SexeEnum

class Professeur(Document):
    id: int
    nom: str
    prenom: Optional[str]
    date_naissance: datetime
    adresse: Optional[str]
    sexe: SexeEnum

    class Settings:
        collection = "professeurs"

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nom": "GERMAIN",
                "prenom": "Christophe",
                "date_naissance": "1971-01-01T23:00:00",
                "adresse": "15 rue du printemps 59000 LILLE",
                "sexe": "HOMME"
            }
        }
