from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from .py_object_id import PyObjectId


class MatiereBase(BaseModel):
    nom: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nom": "LECTURE-CP"
            }
        }


class MatiereCreate(MatiereBase):
    pass


class MatiereUpdate(BaseModel):
    nom: Optional[str] = None


class MatiereResponse(MatiereBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed=True,
        json_schema_extra = {
            "example": {
                "_id": str(ObjectId()),
                "nom": "LECTURE-CP"
            }
        }