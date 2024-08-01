from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.professeur_schema import ProfesseurSchema, UpdateProfesseurSchema
from app.services.professeur_service import (
    get_professeur,
    get_professeurs,
    create_professeur,
    update_professeur,
    delete_professeur,
)

router = APIRouter(prefix="/professeurs", tags=["Professeurs"])

@router.get("/", response_model=List[ProfesseurSchema])
async def read_professeurs():
    return await get_professeurs()

@router.get("/{professeur_id}", response_model=ProfesseurSchema)
async def read_professeur(professeur_id: str):
    professeur = await get_professeur(professeur_id)
    if not professeur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No teacher with id '{professeur_id}'")
    return professeur

@router.post("/", response_model=ProfesseurSchema)
async def create_professeur_endpoint(professeur_data: ProfesseurSchema):
    return await create_professeur(professeur_data)

@router.put("/{professeur_id}", response_model=ProfesseurSchema)
async def update_professeur_endpoint(professeur_id: str, professeur_data: UpdateProfesseurSchema):
    updated_professeur = await update_professeur(professeur_id, professeur_data)
    if not updated_professeur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No teacher with id '{professeur_id}'")
    return updated_professeur

@router.delete("/{professeur_id}", response_model=dict)
async def delete_professeur_endpoint(professeur_id: str):
    if not await delete_professeur(professeur_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No teacher with id '{professeur_id}'")
    return {"detail": "Teacher deleted"}
