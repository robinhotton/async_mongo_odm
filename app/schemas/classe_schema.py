from pydantic import BaseModel, Field
from typing import Optional

class ClasseSchema(BaseModel):
    id: int
    nom: Optional[str] = None
    prof: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nom": "CP",
                "prof": 1
            }
        }

class UpdateClasseSchema(BaseModel):
    nom: Optional[str] = None
    prof: Optional[int] = None
