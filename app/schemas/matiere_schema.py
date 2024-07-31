from pydantic import BaseModel, Field
from typing import Optional

class MatiereSchema(BaseModel):
    idmatiere: int
    nom: str

    class Config:
        json_schema_extra = {
            "example": {
                "idmatiere": 1,
                "nom": "LECTURE-CP"
            }
        }

class UpdateMatiereSchema(BaseModel):
    nom: Optional[str] = None
