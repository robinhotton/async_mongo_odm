from beanie import Document

class Matiere(Document):
    idmatiere: int
    nom: str

    class Settings:
        collection = "matieres"

    class Config:
        schema_extra = {
            "example": {
                "idmatiere": 1,
                "nom": "LECTURE-CP"
            }
        }
