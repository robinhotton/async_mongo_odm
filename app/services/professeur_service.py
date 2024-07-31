from app.models.professeur import Professeur
from app.schemas.professeur_schema import ProfesseurSchema, UpdateProfesseurSchema
from typing import List, Optional

async def get_professeur(professeur_id: int) -> Optional[Professeur]:
    return await Professeur.get(professeur_id)

async def get_professeurs() -> List[Professeur]:
    return await Professeur.find_all().to_list()

async def create_professeur(professeur_data: ProfesseurSchema) -> Professeur:
    professeur = Professeur(**professeur_data.dict())
    await professeur.insert()
    return professeur

async def update_professeur(professeur_id: int, professeur_data: UpdateProfesseurSchema) -> Optional[Professeur]:
    professeur = await Professeur.get(professeur_id)
    if professeur:
        update_data = professeur_data.dict(exclude_unset=True)
        await professeur.set(update_data)
        return professeur
    return None

async def delete_professeur(professeur_id: int) -> bool:
    professeur = await Professeur.get(professeur_id)
    if professeur:
        await professeur.delete()
        return True
    return False
