from fastapi import APIRouter, HTTPException, status
from typing import List
from ..schemas import ClasseSchema, UpdateClasseSchema, CreateClasseSchema
from ..services import get_classe, get_classes, create_classe, update_classe, delete_classe
from bson import ObjectId


router = APIRouter(prefix="/classes", tags=["Classes"])


@router.get("/", response_model=List[ClasseSchema], status_code=status.HTTP_200_OK)
async def read_classes() -> List[ClasseSchema]:
    return await get_classes()


@router.get("/{classe_id}", response_model=ClasseSchema, status_code=status.HTTP_200_OK)
async def read_classe(classe_id: str) -> ClasseSchema:
    if not ObjectId.is_valid(classe_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    classe = await get_classe(classe_id)
    if not classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No class with id '{classe_id}'")
    return classe


@router.post("/", response_model=ClasseSchema, status_code=status.HTTP_201_CREATED)
async def create_classe_endpoint(classe_data: CreateClasseSchema) -> ClasseSchema:
    return await create_classe(classe_data)


@router.put("/{classe_id}", response_model=ClasseSchema, status_code=status.HTTP_200_OK)
async def update_classe_endpoint(classe_id: str, classe_data: UpdateClasseSchema) -> ClasseSchema:
    updated_classe = await update_classe(classe_id, classe_data)
    if not updated_classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No class with id '{classe_id}'")
    return updated_classe


@router.delete("/{classe_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_classe_endpoint(classe_id: str) -> dict:
    if not await delete_classe(classe_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No class with id '{classe_id}'")
    return {"detail": "Class deleted"}