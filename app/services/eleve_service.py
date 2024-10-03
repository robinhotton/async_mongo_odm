from typing import List, Optional
from bson import ObjectId
from ..models import Eleve
from ..schemas import EleveResponse, EleveCreate, EleveUpdate


async def get_eleves() -> List[EleveResponse]:
    eleves: List[Eleve] = await Eleve.find_all().to_list()
    response: List[EleveResponse] = [EleveResponse(_id=str(eleve.id), **eleve.model_dump()) for eleve in eleves]
    return response


async def get_eleve(eleve_id: ObjectId) -> Optional[EleveResponse]:
    eleve: Eleve = await Eleve.get(eleve_id)
    response: EleveResponse = EleveResponse(_id=str(eleve.id), **eleve.model_dump())
    return response


async def create_eleve(eleve_data: EleveCreate) -> EleveResponse:
    eleve: Eleve = Eleve(**eleve_data.model_dump())
    await eleve.insert()
    response: EleveResponse = EleveResponse(_id=str(eleve.id), **eleve_data.model_dump())
    return response


async def update_eleve(eleve_id: ObjectId, eleve_data: EleveUpdate) -> Optional[EleveResponse]:
    eleve: Eleve = await get_eleve(eleve_id)
    if eleve:
        update_data: EleveUpdate = eleve_data.model_dump(exclude_unset=True)
        await eleve.set(update_data)
        response: EleveResponse = EleveResponse(_id=str(eleve.id), **eleve.model_dump())
        return response
    return None


async def delete_eleve(eleve_id: ObjectId) -> bool:
    eleve: Eleve = await get_eleve(eleve_id)
    if eleve:
        await eleve.delete()
        return True
    return False