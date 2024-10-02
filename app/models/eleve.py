from beanie import Document, Link
from typing import Optional
from datetime import datetime
from bson import ObjectId
from ..enums import SexeEnum


class Eleve(Document):
    nom: str
    prenom: Optional[str] = None
    classe: Optional[Link["Classe"]] = None
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
                "classe": str(ObjectId()),  # Référence à la classe
                "date_naissance": "2015-01-01T23:00:00",
                "adresse": "15 rue du Lac 75001 Paris",
                "sexe": SexeEnum.FEMME
            }
        }
