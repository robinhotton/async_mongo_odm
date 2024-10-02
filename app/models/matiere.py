from beanie import Document, BackLink
from typing import TYPE_CHECKING, List
from pydantic import Field


# Pour éviter les problèmes d'importation circulaire
if TYPE_CHECKING:
    from .note import Notes
    

class Matiere(Document):
    nom: str
    notes: List[BackLink["Note"]] = Field(original_field="matiere")

    class Settings:
        collection = "matieres"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "Mathématiques"
            }
        }