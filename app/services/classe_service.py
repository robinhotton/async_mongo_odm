from app.models.classe import Classe
from app.schemas.classe_schema import ClasseSchema, UpdateClasseSchema
from typing import List, Optional

async def get_classe(classe_id: int) -> Optional[Classe]:
    return await Classe.get(classe_id)

async def get_classes() -> List[Classe]:
    return await Classe.find_all().to_list()

async def create_classe(classe_data: ClasseSchema) -> Classe:
    classe = Classe(**classe_data.dict())
    await classe.insert()
    return classe

async def update_classe(classe_id: int, classe_data: UpdateClasseSchema) -> Optional[Classe]:
    classe = await Classe.get(classe_id)
    if classe:
        update_data = classe_data.dict(exclude_unset=True)
        await classe.set(update_data)
        return classe
    return None

async def delete_classe(classe_id: int) -> bool:
    classe = await Classe.get(classe_id)
    if classe:
        await classe.delete()
        return True
    return False
