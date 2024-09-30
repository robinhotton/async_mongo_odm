from datetime import datetime
from beanie import Document
from typing import Optional
from bson import ObjectId
from app.enum.sexe_enum import SexeEnum
from pydantic import Field

class Eleve(Document):
    nom: str
    prenom: Optional[str] = None
    classe: Optional[ObjectId] = Field(None, alias="classe_id")  # Référence à l'ID de la classe
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Settings:
        collection = "eleves"

    class Config:
        schema_extra = {
            "example": {
                "nom": "Durand",
                "prenom": "Marie",
                "classe_id": "60d21b4667d0d8992e610c85",  # Exemple d'ObjectId de la classe
                "date_naissance": "2015-01-01T23:00:00",
                "adresse": "15 rue du Lac 75001 Paris",
                "sexe": "FEMME"
            }
        }
