from typing import List, Optional
from bson import ObjectId
from ..models import Trimestre
from ..schemas import TrimestreResponse, TrimestreCreate, TrimestreUpdate


def _create_response(trimestre: Trimestre) -> TrimestreResponse:
    reponse: TrimestreResponse = TrimestreResponse(
        _id=str(trimestre.id),
        nom=trimestre.nom,
        date=trimestre.date)
    return reponse


async def get_trimestres(skip: int, limit: int) -> List[Trimestre]:
    trimestres: List[Trimestre] = await Trimestre.find_all().skip(skip).limit(limit).to_list()
    response: List[TrimestreResponse] = [_create_response(trimestre) for trimestre in trimestres]
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