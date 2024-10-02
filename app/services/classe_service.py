from ..models import Classe
from ..schemas import ClasseSchema, UpdateClasseSchema, CreateClasseSchema
from bson import ObjectId
from typing import List, Optional


async def validate_object_id(classe_id: str) -> bool:
    return ObjectId.is_valid(classe_id)


async def get_classe(classe_id: str) -> Optional[ClasseSchema]:
    if not await validate_object_id(classe_id):
        return None
    classe: Classe = await Classe.get(ObjectId(classe_id))
    return classe if classe else None


async def get_classes() -> List[ClasseSchema]:
    classes: List[Classe] = await Classe.find_all().to_list()
    return [ClasseSchema(
        _id=str(element.id),
        nom=element.nom,
        prof=str(element.prof.id) if element.prof else None  # Référence au professeur
    ) for element in classes]


async def create_classe(classe_data: CreateClasseSchema) -> ClasseSchema:
    classe: Classe = Classe(**classe_data.model_dump())
    await classe.insert()
    return classe


async def update_classe(classe_id: str, classe_data: UpdateClasseSchema) -> Optional[ClasseSchema]:
    classe: Classe = await get_classe(classe_id)
    if classe:
        update_data = classe_data.model_dump(exclude_unset=True)
        await classe.set(update_data)
        return classe
    return None


async def delete_classe(classe_id: str) -> bool:
    classe: Classe = await get_classe(classe_id)
    if classe:
        await classe.delete()
        return True
    return False
