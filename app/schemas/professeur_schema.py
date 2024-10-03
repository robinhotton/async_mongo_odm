from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from ..enums import SexeEnum
from .py_object_id import PyObjectId


class ProfesseurBase(BaseModel):
    nom: str
    prenom: Optional[str] = None
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nom": "GERMAIN",
                "prenom": "Christophe",
                "date_naissance": "1971-01-01T23:00:00",
                "adresse": "15 rue du printemps 59000 LILLE",
                "sexe": SexeEnum.HOMME
            }
        }


class ProfesseurCreate(ProfesseurBase):
    pass


class ProfesseurUpdate(ProfesseurBase):
    nom: Optional[str] = None
    date_naissance: Optional[datetime] = None
    sexe: Optional[SexeEnum] = None


class ProfesseurResponse(ProfesseurBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed=True,
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "nom": "GERMAIN",
                "prenom": "Christophe",
                "date_naissance": "1971-01-01T23:00:00",
                "adresse": "15 rue du printemps 59000 LILLE",
                "sexe": SexeEnum.HOMME
            }
        }