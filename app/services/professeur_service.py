from typing import List, Optional
from bson import ObjectId
from ..models import Professeur
from ..schemas import ProfesseurResponse, ProfesseurCreate, ProfesseurUpdate


async def get_professeurs() -> List[ProfesseurResponse]:
    professeurs: List[Professeur] = await Professeur.find_all().to_list()
    response: List[ProfesseurResponse] = [ProfesseurResponse(_id=str(professeur.id), **professeur.model_dump()) for professeur in professeurs]
    return response


async def get_professeur(professeur_id: ObjectId) -> Optional[ProfesseurResponse]:
    professeur: Professeur = await Professeur.get(professeur_id)
    response: ProfesseurResponse = ProfesseurResponse(_id=str(professeur.id), **professeur.model_dump())
    return response


async def create_professeur(professeur_data: ProfesseurCreate) -> ProfesseurResponse:
    professeur: Professeur = Professeur(**professeur_data.model_dump())
    await professeur.insert()
    response: ProfesseurResponse = ProfesseurResponse(_id=str(professeur.id), **professeur_data.model_dump())
    return response


async def update_professeur(professeur_id: ObjectId, professeur_data: ProfesseurUpdate) -> Optional[ProfesseurResponse]:
    professeur: Professeur = await Professeur.get(professeur_id)
    if professeur:
        update_data: ProfesseurUpdate = professeur_data.model_dump(exclude_unset=True)
        await professeur.set(update_data)
        response: ProfesseurResponse = ProfesseurResponse(_id=str(professeur.id), **professeur.model_dump())
        return response
    return None


async def delete_professeur(professeur_id: ObjectId) -> bool:
    professeur: Professeur = await Professeur.get(professeur_id)
    if professeur:
        await professeur.delete()
        return True
    return False