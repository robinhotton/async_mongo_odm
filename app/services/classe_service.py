from app.models.classe import Classe
from app.schemas.classe_schema import ClasseSchema, UpdateClasseSchema
from bson import ObjectId
from typing import List, Optional


async def get_classe(classe_id: str) -> Optional[ClasseSchema]:
    if not ObjectId.is_valid(classe_id):
        return None
    classe: Classe = await Classe.get(ObjectId(classe_id))  # Typage ajouté ici
    return ClasseSchema.model_validate(classe) if classe else None


async def get_classes() -> List[ClasseSchema]:
    classes: List[Classe] = await Classe.find_all().to_list()  # Typage ajouté ici
    return [ClasseSchema.model_validate(classe) for classe in classes]


async def create_classe(classe_data: ClasseSchema) -> ClasseSchema:
    classe: Classe = Classe(**classe_data.model_dump())  # Typage ajouté ici
    await classe.insert()
    return ClasseSchema.model_validate(classe)


async def update_classe(classe_id: str, classe_data: UpdateClasseSchema) -> Optional[ClasseSchema]:
    classe: Classe = await get_classe(classe_id)  # Typage ajouté ici
    if classe:
        update_data = classe_data.model_dump(exclude_unset=True)  # Utilisation de model_dump
        await classe.set(update_data)
        return ClasseSchema.model_validate(classe)
    return None


async def delete_classe(classe_id: str) -> bool:
    classe: Classe = await get_classe(classe_id)  # Typage ajouté ici
    if classe:
        await classe.delete()
        return True
    return False
