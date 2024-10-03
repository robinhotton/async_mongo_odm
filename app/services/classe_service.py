from typing import List, Optional
from bson import ObjectId
from ..models import Classe
from ..schemas import ClasseResponse, ClasseCreate, ClasseUpdate


async def get_classes() -> List[ClasseResponse]:
    classes: List[Classe] = await Classe.find_all().to_list()
    response: List[ClasseResponse] = [ClasseResponse(_id=str(classe.id), **classe.model_dump()) for classe in classes]
    return response


async def get_classe(classe_id: ObjectId) -> Optional[ClasseResponse]:
    classe: Classe = await Classe.get(classe_id)
    response: ClasseResponse = ClasseResponse(_id=str(classe.id), **classe.model_dump())
    return response


async def create_classe(classe_data: ClasseCreate) -> ClasseResponse:
    classe: Classe = Classe(**classe_data.model_dump())
    await classe.insert()
    response: ClasseResponse = ClasseResponse(_id=str(classe.id), **classe_data.model_dump())
    return response


async def update_classe(classe_id: ObjectId, classe_data: ClasseUpdate) -> Optional[Classe]:
    classe: Classe = await Classe.get(classe_id)
    if classe:
        update_data: ClasseUpdate = classe_data.model_dump(exclude_unset=True)
        await classe.set(update_data)
        response: ClasseResponse = ClasseResponse(_id=str(classe.id), **classe.model_dump())
        return response
    return None


async def delete_classe(classe_id: ObjectId) -> bool:
    classe: Classe = await Classe.get(classe_id)
    if classe:
        await classe.delete()
        return True
    return False