from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from ..schemas import MatiereResponse, MatiereCreate, MatiereUpdate
from ..services import get_matiere, get_matieres, create_matiere, update_matiere, delete_matiere


router = APIRouter(prefix="/matieres", tags=["Matieres"])


@router.get("/", response_model=List[MatiereResponse], status_code=status.HTTP_200_OK)
async def read_matieres() -> List[MatiereResponse]:
    return await get_matieres()


@router.get("/{matiere_id}", response_model=MatiereResponse, status_code=status.HTTP_200_OK)
async def read_matiere(matiere_id: str) -> MatiereResponse:
    if not ObjectId.is_valid(matiere_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    matiere = await get_matiere(ObjectId(matiere_id))
    if not matiere:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No subject with id '{matiere_id}'")
    return matiere


@router.post("/", response_model=MatiereResponse, status_code=status.HTTP_201_CREATED)
async def create_matiere_endpoint(matiere_data: MatiereCreate) -> MatiereResponse:
    return await create_matiere(matiere_data)


@router.put("/{matiere_id}", response_model=MatiereResponse, status_code=status.HTTP_200_OK)
async def update_matiere_endpoint(matiere_id: str, matiere_data: MatiereUpdate) -> MatiereResponse:
    if not ObjectId.is_valid(matiere_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    updated_matiere = await update_matiere(ObjectId(matiere_id), matiere_data)
    if not updated_matiere:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No subject with id '{matiere_id}'")
    return updated_matiere


@router.delete("/{matiere_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_matiere_endpoint(matiere_id: str) -> dict:
    if not ObjectId.is_valid(matiere_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    if not await delete_matiere(ObjectId(matiere_id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No subject with id '{matiere_id}'")
    return {"detail": "Subject deleted"}