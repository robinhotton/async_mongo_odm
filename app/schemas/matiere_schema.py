from bson import ObjectId
from pydantic import BaseModel
from typing import Optional

class MatiereBaseSchema(BaseModel):
    nom: str

    class Config:
        from_attributes = True

class CreateMatiereSchema(MatiereBaseSchema):
    pass

class UpdateMatiereSchema(BaseModel):
    nom: Optional[str] = None

class MatiereSchema(MatiereBaseSchema):
    id_matiere: str

    class Config:
        json_schema_extra = {
            "example": {
                "id_matiere": str(ObjectId()),
                "nom": "LECTURE-CP"
            }
        }
