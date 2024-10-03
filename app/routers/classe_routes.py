from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from ..schemas import ClasseResponse, ClasseCreate, ClasseUpdate
from ..services import get_classe, get_classes, create_classe, update_classe, delete_classe


router = APIRouter(prefix="/classes", tags=["Classes"])


def _verify_object_id(object_id: str) -> ObjectId:
    if not ObjectId.is_valid(object_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    return ObjectId(object_id)


def _response_not_none(response: ClasseResponse, classe_id: ObjectId) -> None:
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No class with id '{classe_id}'")


@router.get("/", response_model=List[ClasseResponse], status_code=status.HTTP_200_OK)
async def read_classes(skip: int = 0, limit: int = 10) -> List[ClasseResponse]:
    return await get_classes(skip, limit)


@router.get("/{classe_id}", response_model=ClasseResponse, status_code=status.HTTP_200_OK)
async def read_classe(classe_id: str) -> ClasseResponse:
    classe_id = _verify_object_id(classe_id)
    classe = await get_classe(classe_id)
    _response_not_none(classe, classe_id)
    return classe


@router.post("/", response_model=ClasseResponse, status_code=status.HTTP_201_CREATED)
async def create_classe_endpoint(classe_data: ClasseCreate) -> ClasseResponse:
    return await create_classe(classe_data)


@router.put("/{classe_id}", response_model=ClasseResponse, status_code=status.HTTP_200_OK)
async def update_classe_endpoint(classe_id: str, classe_data: ClasseUpdate) -> ClasseResponse:
    classe_id = _verify_object_id(classe_id)
    updated_classe: ClasseUpdate = await update_classe(classe_id, classe_data)
    _response_not_none(updated_classe, classe_id)
    return updated_classe


@router.delete("/{classe_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_classe_endpoint(classe_id: str) -> dict:
    classe_id = _verify_object_id(classe_id)
    deleted_classe: bool = await delete_classe(classe_id)
    _response_not_none(deleted_classe, classe_id)
    return {"message": f"Class with id '{classe_id}' deleted successfully"}