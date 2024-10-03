from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from ..schemas import ProfesseurResponse, ProfesseurCreate, ProfesseurUpdate
from ..services import get_professeur, get_professeurs, create_professeur, update_professeur, delete_professeur


router = APIRouter(prefix="/professeurs", tags=["Professeurs"])


@router.get("/", response_model=List[ProfesseurResponse], status_code=status.HTTP_200_OK)
async def read_professeurs() -> List[ProfesseurResponse]:
    return await get_professeurs()


@router.get("/{professeur_id}", response_model=ProfesseurResponse, status_code=status.HTTP_200_OK)
async def read_professeur(professeur_id: str) -> ProfesseurResponse:
    if not ObjectId.is_valid(professeur_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    professeur = await get_professeur(ObjectId(professeur_id))
    if not professeur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No teacher with id '{professeur_id}'")
    return professeur


@router.post("/", response_model=ProfesseurResponse, status_code=status.HTTP_201_CREATED)
async def create_professeur_endpoint(professeur_data: ProfesseurCreate) -> ProfesseurResponse:
    return await create_professeur(professeur_data)


@router.put("/{professeur_id}", response_model=ProfesseurResponse, status_code=status.HTTP_200_OK)
async def update_professeur_endpoint(professeur_id: str, professeur_data: ProfesseurUpdate) -> ProfesseurResponse:
    if not ObjectId.is_valid(professeur_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    updated_professeur = await update_professeur(ObjectId(professeur_id), professeur_data)
    if not updated_professeur:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No teacher with id '{professeur_id}'")
    return updated_professeur


@router.delete("/{professeur_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_professeur_endpoint(professeur_id: str) -> dict:
    if not ObjectId.is_valid(professeur_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    if not await delete_professeur(ObjectId(professeur_id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No teacher with id '{professeur_id}'")
    return {"detail": "Teacher deleted"}