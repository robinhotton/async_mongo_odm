from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .py_object_id import PyObjectId


class NoteBase(BaseModel):
    date_saisie: datetime
    eleve: Optional[str] = Field(default=None, alias="eleve_id")
    matiere: Optional[str] = Field(default=None, alias="matiere_id")
    prof: Optional[str] = Field(default=None, alias="prof_id")
    trimestre: Optional[str] = Field(default=None, alias="trimestre_id")
    note: int
    avis: str
    avancement: float

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "date_saisie": "2019-10-15T08:07:03",
                "eleve_id": str(ObjectId()),
                "matiere_id": str(ObjectId()),
                "prof_id": str(ObjectId()),
                "trimestre_id": str(ObjectId()),
                "note": 12,
                "avis": "Travail à approfondir",
                "avancement": 0.0
            }
        }


class NoteCreate(NoteBase):
    pass


class NoteUpdate(BaseModel):
    date_saisie: Optional[datetime] = None
    note: Optional[int] = None
    avis: Optional[str] = None
    avancement: Optional[float] = None


class NoteResponse(NoteBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed=True,
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "date_saisie": "2019-10-15T08:07:03",
                "eleve_id": str(ObjectId()),
                "matiere_id": str(ObjectId()),
                "prof_id": str(ObjectId()),
                "trimestre_id": str(ObjectId()),
                "note": 12,
                "avis": "Travail à approfondir",
                "avancement": 0.0
            }
        }
