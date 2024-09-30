from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.enum.sexe_enum import SexeEnum

class EleveBaseSchema(BaseModel):
    nom: str
    prenom: Optional[str] = None
    classe: Optional[str] = Field(None, alias="classe_id")
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        populate_by_name = True

class CreateEleveSchema(EleveBaseSchema):
    pass

class UpdateEleveSchema(EleveBaseSchema):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    classe: Optional[str] = Field(None, alias="classe_id")
    date_naissance: Optional[datetime] = None
    adresse: Optional[str] = None
    sexe: Optional[SexeEnum] = None

class EleveSchema(EleveBaseSchema):
    id: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": str(ObjectId()),
                "nom": "Durand",
                "prenom": "Marie",
                "classe_id": str(ObjectId()),
                "date_naissance": "2015-01-01T23:00:00",
                "adresse": "15 rue du Lac 75001 Paris",
                "sexe": "FEMME"
            }
        }
