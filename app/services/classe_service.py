from ..models import Classe
from ..schemas import ClasseResponse, ClasseCreate, ClasseUpdate
from bson import ObjectId
from typing import List, Optional


async def validate_object_id(classe_id: str) -> bool:
    return ObjectId.is_valid(classe_id)


async def get_classe(classe_id: str) -> Optional[ClasseResponse]:
    if not await validate_object_id(classe_id):
        return None
    classe: Classe = await Classe.get(ObjectId(classe_id))
    response = ClasseResponse(_id=str(classe.id), **classe.model_dump())
    return response


async def get_classes() -> List[ClasseResponse]:
    classes: List[Classe] = await Classe.find_all().to_list()
    return [ClasseResponse(_id=str(classe.id), **classe.model_dump()) for classe in classes]


async def create_classe(classe_data: ClasseCreate) -> ClasseResponse:
    classe: Classe = Classe(**classe_data.model_dump())
    await classe.insert()
    response = ClasseResponse(_id=str(classe.id), **classe_data.model_dump())
    return response


async def update_classe(classe_id: str, classe_data: ClasseUpdate) -> Optional[Classe]:
    if not await validate_object_id(classe_id):
        return None
    
    classe: Classe = await Classe.get(ObjectId(classe_id))
    if classe:
        update_data = classe_data.model_dump(exclude_unset=True)
        await classe.set(update_data)
        response = ClasseResponse(_id=str(classe.id), **classe.model_dump())
        return response
    return None


async def delete_classe(classe_id: str) -> bool:
    if not await validate_object_id(classe_id):
        return None
    
    classe: Classe = await Classe.get(ObjectId(classe_id))
    if classe:
        await classe.delete()
        return True
    return False
