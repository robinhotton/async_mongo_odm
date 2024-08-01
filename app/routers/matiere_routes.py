from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.matiere_schema import MatiereSchema, UpdateMatiereSchema
from app.services.matiere_service import (
    get_matiere,
    get_matieres,
    create_matiere,
    update_matiere,
    delete_matiere,
)

router = APIRouter(prefix="/matieres", tags=["Matieres"])

@router.get("/", response_model=List[MatiereSchema])
async def read_matieres():
    return await get_matieres()

@router.get("/{matiere_id}", response_model=MatiereSchema)
async def read_matiere(matiere_id: str):
    matiere = await get_matiere(matiere_id)
    if not matiere:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No subject with id '{matiere_id}'")
    return matiere

@router.post("/", response_model=MatiereSchema)
async def create_matiere_endpoint(matiere_data: MatiereSchema):
    return await create_matiere(matiere_data)

@router.put("/{matiere_id}", response_model=MatiereSchema)
async def update_matiere_endpoint(matiere_id: str, matiere_data: UpdateMatiereSchema):
    updated_matiere = await update_matiere(matiere_id, matiere_data)
    if not updated_matiere:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No subject with id '{matiere_id}'")
    return updated_matiere

@router.delete("/{matiere_id}", response_model=dict)
async def delete_matiere_endpoint(matiere_id: str):
    if not await delete_matiere(matiere_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No subject with id '{matiere_id}'")
    return {"detail": "Subject deleted"}
