from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.enum.sexe_enum import SexeEnum

class ProfesseurBaseSchema(BaseModel):
    nom: str
    prenom: Optional[str] = None
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        populate_by_name = True

class CreateProfesseurSchema(ProfesseurBaseSchema):
    pass

class UpdateProfesseurSchema(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    date_naissance: Optional[datetime] = None
    adresse: Optional[str] = None
    sexe: Optional[SexeEnum] = None

class ProfesseurSchema(ProfesseurBaseSchema):
    id: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": str(ObjectId()),
                "nom": "GERMAIN",
                "prenom": "Christophe",
                "date_naissance": "1971-01-01T23:00:00",
                "adresse": "15 rue du printemps 59000 LILLE",
                "sexe": "HOMME"
            }
        }
