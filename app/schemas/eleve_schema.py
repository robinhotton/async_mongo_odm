from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.models.eleve import SexeEnum

class EleveSchema(BaseModel):
    id: int
    nom: str
    prenom: Optional[str] = None
    classe: int
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Config:
        json_schema_extra = {
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

class UpdateEleveSchema(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    classe: Optional[int] = None
    date_naissance: Optional[datetime] = None
    adresse: Optional[str] = None
    sexe: Optional[SexeEnum] = None
