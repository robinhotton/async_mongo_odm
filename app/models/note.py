from datetime import datetime
from beanie import Document

class Notes(Document):
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

    class Settings:
        collection = "notes"

    class Config:
        schema_extra = {
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
