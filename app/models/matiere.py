from beanie import Document


class Matiere(Document):
    nom: str

    class Settings:
        collection = "matieres"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "LECTURE-CP"
            }
        }