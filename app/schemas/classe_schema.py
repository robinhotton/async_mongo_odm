from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from .py_object_id import PyObjectId


class ClasseBase(BaseModel):
    nom: str = None
    prof: Optional[str] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nom": "CP",
                "prof": str(ObjectId())
            }
        }
        

class ClasseCreate(ClasseBase):
    pass


class ClasseUpdate(ClasseBase):
    nom: Optional[str] = None


class ClasseResponse(ClasseBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed=True,
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "nom": "CP",
                "prof": str(ObjectId())
            }
        }