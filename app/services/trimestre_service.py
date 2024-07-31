from app.models.trimestre import Trimestre
from app.schemas.trimestre_schema import TrimestreSchema, UpdateTrimestreSchema
from typing import List, Optional

async def get_trimestre(trimestre_id: int) -> Optional[Trimestre]:
    return await Trimestre.get(trimestre_id)

async def get_trimestres() -> List[Trimestre]:
    return await Trimestre.find_all().to_list()

async def create_trimestre(trimestre_data: TrimestreSchema) -> Trimestre:
    trimestre = Trimestre(**trimestre_data.dict())
    await trimestre.insert()
    return trimestre

async def update_trimestre(trimestre_id: int, trimestre_data: UpdateTrimestreSchema) -> Optional[Trimestre]:
    trimestre = await Trimestre.get(trimestre_id)
    if trimestre:
        update_data = trimestre_data.dict(exclude_unset=True)
        await trimestre.set(update_data)
        return trimestre
    return None

async def delete_trimestre(trimestre_id: int) -> bool:
    trimestre = await Trimestre.get(trimestre_id)
    if trimestre:
        await trimestre.delete()
        return True
    return False
