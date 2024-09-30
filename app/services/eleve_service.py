from ..models import Eleve
from ..schemas import EleveSchema, UpdateEleveSchema
from typing import List, Optional
from bson import ObjectId


async def get_eleve(eleve_id: str) -> Optional[EleveSchema]:
    if not ObjectId.is_valid(eleve_id):
        return None
    eleve = await Eleve.get(ObjectId(eleve_id))
    return EleveSchema.model_validate(eleve) if eleve else None


async def get_eleves() -> List[EleveSchema]:
    eleves: List[Eleve] = await Eleve.find_all().to_list()
    return [EleveSchema.model_validate(eleve) for eleve in eleves]


async def create_eleve(eleve_data: EleveSchema) -> EleveSchema:
    eleve = Eleve(**eleve_data.model_dump())
    await eleve.insert()
    return EleveSchema.model_validate(eleve)


async def update_eleve(eleve_id: str, eleve_data: UpdateEleveSchema) -> Optional[EleveSchema]:
    eleve = await get_eleve(eleve_id)
    if eleve:
        update_data = eleve_data.model_dump(exclude_unset=True)
        await eleve.set(update_data)
        return EleveSchema.model_validate(eleve)
    return None


async def delete_eleve(eleve_id: str) -> bool:
    eleve = await get_eleve(eleve_id)
    if eleve:
        await eleve.delete()
        return True
    return False
