from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TrimestreSchema(BaseModel):
    idtrimestre: int
    nom: str
    date: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "idtrimestre": 1,
                "nom": "TRIM01",
                "date": "2023-12-01T09:08:03"
            }
        }

class UpdateTrimestreSchema(BaseModel):
    nom: Optional[str] = None
    date: Optional[datetime] = None
