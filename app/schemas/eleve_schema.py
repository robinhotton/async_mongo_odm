from bson import ObjectId
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from ..enums import SexeEnum


class EleveBaseSchema(BaseModel):
    nom: str
    prenom: Optional[str] = None
    classe_id: Optional[str] = None
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Config:
        from_attributes = True


class CreateEleveSchema(EleveBaseSchema):
    pass


class UpdateEleveSchema(EleveBaseSchema):
    nom: Optional[str] = None
    date_naissance: Optional[datetime] = None
    sexe: Optional[SexeEnum] = None


class EleveSchema(EleveBaseSchema):
    _id: str

    class Config:
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "nom": "Durand",
                "prenom": "Marie",
                "classe_id": str(ObjectId()),
                "date_naissance": "2015-01-01T23:00:00",
                "adresse": "15 rue du Lac 75001 Paris",
                "sexe": SexeEnum.FEMME
            }
        }