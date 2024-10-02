from beanie import Document, BackLink
from typing import TYPE_CHECKING, List
from datetime import datetime
from pydantic import Field


class Trimestre(Document):
    nom: str
    date: datetime
    notes: List[BackLink["Note"]] = Field(original_field="trimestre")

    class Settings:
        collection = "trimestres"

    class Config:
        json_schema_extra = {
            "example": {
                "nom": "TRIM01",
                "date": "2023-12-01T09:08:03"
            }
        }
