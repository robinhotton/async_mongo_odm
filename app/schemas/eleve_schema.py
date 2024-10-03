from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from ..enums import SexeEnum
from .py_object_id import PyObjectId


class EleveBase(BaseModel):
    nom: str
    prenom: Optional[str] = None
    classe: Optional[str] = Field(default=None, alias="classe_id")
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nom": "Durand",
                "prenom": "Marie",
                "classe_id": str(ObjectId()),
                "date_naissance": "2015-01-01T23:00:00",
                "adresse": "15 rue du Lac 75001 Paris",
                "sexe": SexeEnum.FEMME
            }
        }


class EleveCreate(EleveBase):
    pass


class EleveUpdate(EleveBase):
    nom: Optional[str] = None
    date_naissance: Optional[datetime] = None
    sexe: Optional[SexeEnum] = None


class EleveResponse(EleveBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed=True,
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