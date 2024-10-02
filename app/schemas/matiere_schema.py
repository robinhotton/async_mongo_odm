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
    _id: str

    class Config:
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "nom": "LECTURE-CP"
            }
        }