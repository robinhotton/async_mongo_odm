from datetime import datetime
from beanie import Document, Link
from typing import Optional
from bson import ObjectId
from .eleve import Eleve
from .classe import Classe
from .matiere import Matiere
from .professeur import Professeur
from .trimestre import Trimestre


class Notes(Document):
    date_saisie: datetime
    eleve: Optional[Link[Eleve]] = None  # Lien direct vers l'élève
    classe: Optional[Link[Classe]] = None  # Lien direct vers la classe
    matiere: Optional[Link[Matiere]] = None  # Lien direct vers la matière
    prof: Optional[Link[Professeur]] = None  # Lien direct vers le professeur
    trimestre: Optional[Link[Trimestre]] = None  # Lien direct vers le trimestre
    note: int
    avis: str
    avancement: float

    class Settings:
        collection = "notes"

    class Config:
        json_schema_extra = {
            "example": {
                "date_saisie": "2019-10-15T08:07:03",
                "eleve": str(ObjectId()),  # Référence à l'élève
                "classe": str(ObjectId()),  # Référence à la classe
                "matiere": str(ObjectId()),  # Référence à la matière
                "prof": str(ObjectId()),  # Référence au professeur
                "trimestre": str(ObjectId()),  # Référence au trimestre
                "note": 12,
                "avis": "Travail à approfondir",
                "avancement": 0.5
            }
        }