from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.models.sexe_enum import SexeEnum

class ProfesseurSchema(BaseModel):
    id: int
    nom: str
    prenom: Optional[str] = None
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nom": "GERMAIN",
                "prenom": "Christophe",
                "date_naissance": "1971-01-01T23:00:00",
                "adresse": "15 rue du printemps 59000 LILLE",
                "sexe": "HOMME"
            }
        }

class UpdateProfesseurSchema(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    date_naissance: Optional[datetime] = None
    adresse: Optional[str] = None
    sexe: Optional[SexeEnum] = None
