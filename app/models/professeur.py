from beanie import Document, Link, BackLink
from typing import Optional, List
from datetime import datetime
from pydantic import Field
from ..enums import SexeEnum


class Professeur(Document):
    nom: str
    prenom: Optional[str] = None
    date_naissance: datetime
    adresse: Optional[str] = None
    sexe: SexeEnum
    matieres: Optional[List[Link["Matiere"]]] = None
    classes: List[BackLink["Classe"]] = Field(original_field="prof")

    class Settings:
        collection = "professeurs"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "GERMAIN",
                "prenom": "Christophe",
                "date_naissance": "1971-01-01T23:00:00",
                "adresse": "15 rue du printemps 59000 LILLE",
                "sexe": SexeEnum.HOMME
            }
        }
