from typing import List, Optional
from bson import ObjectId
from ..models import Matiere
from ..schemas import MatiereResponse, MatiereCreate, MatiereUpdate


async def get_matieres() -> List[MatiereResponse]:
    matieres: List[Matiere] = await Matiere.find_all().to_list()
    response: List[MatiereResponse] = [MatiereResponse(_id=str(matiere.id), **matiere.model_dump()) for matiere in matieres]
    return response


async def get_matiere(matiere_id: ObjectId) -> Optional[MatiereResponse]:
    matiere: Matiere = await Matiere.get(matiere_id)
    response: MatiereResponse = MatiereResponse(_id=str(matiere.id), **matiere.model_dump())
    return response


async def create_matiere(matiere_data: MatiereCreate) -> MatiereResponse:
    matiere: Matiere = Matiere(**matiere_data.model_dump())
    await matiere.insert()
    response: MatiereResponse = MatiereResponse(_id=str(matiere.id), **matiere_data.model_dump())
    return response


async def update_matiere(matiere_id: ObjectId, matiere_data: MatiereUpdate) -> Optional[MatiereResponse]:
    matiere: Matiere = await Matiere.get(matiere_id)
    if matiere:
        update_data: MatiereUpdate = matiere_data.model_dump(exclude_unset=True)
        await matiere.set(update_data)
        response: MatiereResponse = MatiereResponse(_id=str(matiere.id), **matiere.model_dump())
        return response
    return None


async def delete_matiere(matiere_id: ObjectId) -> bool:
    matiere: Matiere = await Matiere.get(matiere_id)
    if matiere:
        await matiere.delete()
        return True
    return False