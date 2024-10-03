from typing import List, Optional
from bson import ObjectId
from ..models import Trimestre
from ..schemas import TrimestreResponse, TrimestreCreate, TrimestreUpdate


async def get_trimestres() -> List[Trimestre]:
    trimestres: List[Trimestre] = await Trimestre.find_all().to_list()
    response: List[TrimestreResponse] = [TrimestreResponse(_id=str(trimestre.id), **trimestre.model_dump()) for trimestre in trimestres]
    return response


async def get_trimestre(trimestre_id: ObjectId) -> Optional[TrimestreResponse]:
    trimestre: Trimestre = await Trimestre.get(trimestre_id)
    response: TrimestreResponse = TrimestreResponse(_id=str(trimestre.id), **trimestre.model_dump())
    return response


async def create_trimestre(trimestre_data: TrimestreCreate) -> Trimestre:
    trimestre = Trimestre(**trimestre_data.model_dump())
    await trimestre.insert()
    response: TrimestreResponse = TrimestreResponse(_id=str(trimestre.id), **trimestre_data.model_dump())
    return response


async def update_trimestre(trimestre_id: ObjectId, trimestre_data: TrimestreUpdate) -> Optional[Trimestre]:
    trimestre: Trimestre = await Trimestre.get(trimestre_id)
    if trimestre:
        update_data: TrimestreUpdate = trimestre_data.model_dump(exclude_unset=True)
        await trimestre.set(update_data)
        response: TrimestreResponse = TrimestreResponse(_id=str(trimestre.id), **trimestre.model_dump())
        return response
    return None


async def delete_trimestre(trimestre_id: ObjectId) -> bool:
    trimestre: Trimestre = await Trimestre.get(trimestre_id)
    if trimestre:
        await trimestre.delete()
        return True
    return False