from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class ClasseBaseSchema(BaseModel):
    nom: Optional[str] = None
    prof_id: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        

class CreateClasseSchema(ClasseBaseSchema):
    pass


class UpdateClasseSchema(ClasseBaseSchema):
    prof: Optional[str] = Field(None, alias="prof_id")


class ClasseSchema(ClasseBaseSchema):
    _id: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": str(ObjectId()),  # Exemple d'ID de classe
                "nom": "CP",
                "prof_id": str(ObjectId())  # Exemple d'ID de professeur
            }
        }
