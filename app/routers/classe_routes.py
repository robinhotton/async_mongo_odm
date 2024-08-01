from fastapi import APIRouter, HTTPException, Depends, status
from app.dependencies import check_role, get_current_user
from typing import List
from app.schemas.classe_schema import ClasseSchema, UpdateClasseSchema
from app.services.classe_service import (
    get_classe,
    get_classes,
    create_classe,
    update_classe,
    delete_classe,
)

router = APIRouter(prefix="/classes", tags=["Classes"])

@router.get("/", response_model=List[ClasseSchema])
async def read_classes():
    return await get_classes()

@router.get("/{classe_id}", response_model=ClasseSchema)
async def read_classe(classe_id: str):
    classe = await get_classe(classe_id)
    if not classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No class with id '{classe_id}'")
    return classe

@router.post("/", response_model=ClasseSchema)
async def create_classe_endpoint(classe_data: ClasseSchema):
    return await create_classe(classe_data)

@router.put("/{classe_id}", response_model=ClasseSchema)
async def update_classe_endpoint(classe_id: str, classe_data: UpdateClasseSchema):
    updated_classe = await update_classe(classe_id, classe_data)
    if not updated_classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No class with id '{classe_id}'")
    return updated_classe

@router.delete("/{classe_id}", response_model=dict)
async def delete_classe_endpoint(classe_id: str):
    if not await delete_classe(classe_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No class with id '{classe_id}'")
    return {"detail": "Class deleted"}
