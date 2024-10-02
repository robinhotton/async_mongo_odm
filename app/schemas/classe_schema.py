from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional


class ClasseBaseSchema(BaseModel):
    nom: str = None
    prof_id: Optional[str] = Field(None, alias="prof_id")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nom": "CP",
                "prof_id": str(ObjectId())
            }
        }
        

class CreateClasseSchema(ClasseBaseSchema):
    pass


class UpdateClasseSchema(ClasseBaseSchema):
    nom: Optional[str] = None


class ClasseSchema(ClasseBaseSchema):
    _id: str

    class Config:
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "nom": "CP",
                "prof_id": str(ObjectId())
            }
        }