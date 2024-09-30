from bson import ObjectId
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NoteBaseSchema(BaseModel):
    date_saisie: datetime
    id_eleve: str
    id_classe: str
    id_matiere: str
    id_prof: str
    id_trimestre: str
    note: int
    avis: str
    avancement: float

    class Config:
        from_attributes = True
        populate_by_name = True

class CreateNoteSchema(NoteBaseSchema):
    pass

class UpdateNoteSchema(BaseModel):
    date_saisie: Optional[datetime] = None
    id_eleve: Optional[str] = None
    id_classe: Optional[str] = None
    id_matiere: Optional[str] = None
    id_prof: Optional[str] = None
    id_trimestre: Optional[str] = None
    note: Optional[int] = None
    avis: Optional[str] = None
    avancement: Optional[float] = None

class NoteSchema(NoteBaseSchema):
    id_notes: str

    class Config:
        json_schema_extra = {
            "example": {
                "id_notes": str(ObjectId()),
                "date_saisie": "2019-10-15T08:07:03",
                "id_eleve": str(ObjectId()),
                "id_classe": str(ObjectId()),
                "id_matiere": str(ObjectId()),
                "id_prof": str(ObjectId()),
                "id_trimestre": str(ObjectId()),
                "note": 12,
                "avis": "Travail à approfondir",
                "avancement": 0.0
            }
        }
