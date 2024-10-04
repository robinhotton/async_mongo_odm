from fastapi import APIRouter, status
from typing import List
from bson import ObjectId
from ..schemas import ClasseResponse, ClasseCreate, ClasseUpdate
from ..services import get_classe, get_classes, create_classe, update_classe, delete_classe
from .routes_utils import _verify_object_id, _response_not_none


router_name = "classes"
router = APIRouter(prefix=f"/{router_name}", tags=[router_name.capitalize()])


@router.get("/", response_model=List[ClasseResponse], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 100) -> List[ClasseResponse]:
    classes: List[ClasseResponse] = await get_classes(skip, limit)
    return classes


@router.get("/{classe_id}", response_model=ClasseResponse, status_code=status.HTTP_200_OK)
async def read_classe(classe_id: str) -> ClasseResponse:
    classe_id: ObjectId = _verify_object_id(classe_id)
    classe: ClasseResponse = await get_classe(classe_id)
    _response_not_none(classe, classe_id, router_name)
    return classe


@router.post("/", response_model=ClasseResponse, status_code=status.HTTP_201_CREATED)
async def create_classe_endpoint(classe_data: ClasseCreate) -> ClasseResponse:
    classe: ClasseResponse = await create_classe(classe_data)
    return classe


@router.put("/{classe_id}", response_model=ClasseResponse, status_code=status.HTTP_200_OK)
async def update_classe_endpoint(classe_id: str, classe_data: ClasseUpdate) -> ClasseResponse:
    classe_id: ObjectId = _verify_object_id(classe_id)
    updated_classe: ClasseResponse = await update_classe(classe_id, classe_data)
    _response_not_none(updated_classe, classe_id, router_name)
    return updated_classe


@router.delete("/{classe_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_classe_endpoint(classe_id: str) -> dict:
    classe_id: ObjectId = _verify_object_id(classe_id)
    deleted_classe: bool = await delete_classe(classe_id)
    _response_not_none(deleted_classe, classe_id, router_name)
    return {"message": f"Document with id '{classe_id}' deleted successfully"}