from app.models.matiere import Matiere
from app.schemas.matiere_schema import MatiereSchema, UpdateMatiereSchema
from typing import List, Optional

async def get_matiere(matiere_id: int) -> Optional[Matiere]:
    return await Matiere.get(matiere_id)

async def get_matieres() -> List[Matiere]:
    return await Matiere.find_all().to_list()

async def create_matiere(matiere_data: MatiereSchema) -> Matiere:
    matiere = Matiere(**matiere_data.dict())
    await matiere.insert()
    return matiere

async def update_matiere(matiere_id: int, matiere_data: UpdateMatiereSchema) -> Optional[Matiere]:
    matiere = await Matiere.get(matiere_id)
    if matiere:
        update_data = matiere_data.dict(exclude_unset=True)
        await matiere.set(update_data)
        return matiere
    return None

async def delete_matiere(matiere_id: int) -> bool:
    matiere = await Matiere.get(matiere_id)
    if matiere:
        await matiere.delete()
        return True
    return False
