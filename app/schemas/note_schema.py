from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NoteSchema(BaseModel):
    idnotes: int
    date_saisie: datetime
    ideleve: int
    idclasse: int
    idmatiere: int
    idprof: int
    idtrimestre: int
    note: int
    avis: str
    avancement: float

    class Config:
        json_schema_extra = {
            "example": {
                "idnotes": 1,
                "date_saisie": "2019-10-15T08:07:03",
                "ideleve": 2,
                "idclasse": 2,
                "idmatiere": 5,
                "idprof": 2,
                "idtrimestre": 1,
                "note": 12,
                "avis": "Travail à approfondir",
                "avancement": 0
            }
        }

class UpdateNoteSchema(BaseModel):
    date_saisie: Optional[datetime] = None
    ideleve: Optional[int] = None
    idclasse: Optional[int] = None
    idmatiere: Optional[int] = None
    idprof: Optional[int] = None
    idtrimestre: Optional[int] = None
    note: Optional[int] = None
    avis: Optional[str] = None
    avancement: Optional[float] = None
