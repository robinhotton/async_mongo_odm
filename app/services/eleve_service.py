from app.models.eleve import Eleve
from app.schemas.eleve_schema import EleveSchema, UpdateEleveSchema
from typing import List, Optional

async def get_eleve(eleve_id: int) -> Optional[Eleve]:
    return await Eleve.get(eleve_id)

async def get_eleves() -> List[Eleve]:
    return await Eleve.find_all().to_list()

async def create_eleve(eleve_data: EleveSchema) -> Eleve:
    eleve = Eleve(**eleve_data.dict())
    await eleve.insert()
    return eleve

async def update_eleve(eleve_id: int, eleve_data: UpdateEleveSchema) -> Optional[Eleve]:
    eleve = await Eleve.get(eleve_id)
    if eleve:
        update_data = eleve_data.dict(exclude_unset=True)
        await eleve.set(update_data)
        return eleve
    return None

async def delete_eleve(eleve_id: int) -> bool:
    eleve = await Eleve.get(eleve_id)
    if eleve:
        await eleve.delete()
        return True
    return False
