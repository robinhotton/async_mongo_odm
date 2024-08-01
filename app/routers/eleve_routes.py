from fastapi import APIRouter, HTTPException, Depends, status
from app.dependencies import check_role, get_current_user
from typing import List
from app.schemas.eleve_schema import EleveSchema, UpdateEleveSchema
from app.services.eleve_service import (
    get_eleve,
    get_eleves,
    create_eleve,
    update_eleve,
    delete_eleve,
)

router = APIRouter(prefix="/eleves", tags=["Eleves"])

@router.get("/", response_model=List[EleveSchema])
async def read_eleves():
    return await get_eleves()

@router.get("/{eleve_id}", response_model=EleveSchema)
async def read_eleve(eleve_id: str):
    eleve = await get_eleve(eleve_id)
    if not eleve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No student with id '{eleve_id}'")
    return eleve

@router.post("/", response_model=EleveSchema)
async def create_eleve_endpoint(eleve_data: EleveSchema):
    return await create_eleve(eleve_data)

@router.put("/{eleve_id}", response_model=EleveSchema)
async def update_eleve_endpoint(eleve_id: str, eleve_data: UpdateEleveSchema):
    updated_eleve = await update_eleve(eleve_id, eleve_data)
    if not updated_eleve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No student with id '{eleve_id}'")
    return updated_eleve

@router.delete("/{eleve_id}", response_model=dict)
async def delete_eleve_endpoint(eleve_id: str):
    if not await delete_eleve(eleve_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No student with id '{eleve_id}'")
    return {"detail": "Student deleted"}
