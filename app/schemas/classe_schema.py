from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class ClasseBaseSchema(BaseModel):
    nom: Optional[str] = None
    prof: str = Field(default=None, alias="prof_id")

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True  # Autorise les types arbitraires comme ObjectId
        populate_by_name = True  # Autorise l'utilisation des alias

class CreateClasseSchema(ClasseBaseSchema):
    pass

class UpdateClasseSchema(ClasseBaseSchema):
    nom: Optional[str] = None
    prof: Optional[str] = Field(None, alias="prof_id")

class ClasseSchema(ClasseBaseSchema):
    id: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": str(ObjectId()),  # Exemple d'ID de classe
                "nom": "CP",
                "prof_id": str(ObjectId())  # Exemple d'ID de professeur
            }
        }
