from fastapi import APIRouter, HTTPException, status
from ..schemas import EleveSchema, UpdateEleveSchema
from ..services import get_eleve, get_eleves, create_eleve, update_eleve, delete_eleve
from typing import List
from bson import ObjectId


router = APIRouter(prefix="/eleves", tags=["Eleves"])


@router.get("/", response_model=List[EleveSchema], status_code=status.HTTP_200_OK)
async def read_eleves() -> List[EleveSchema]:
    return await get_eleves()


@router.get("/{eleve_id}", response_model=EleveSchema, status_code=status.HTTP_200_OK)
async def read_eleve(eleve_id: str) -> EleveSchema:
    if not ObjectId.is_valid(eleve_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    eleve = await get_eleve(eleve_id)
    if not eleve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No student with id '{eleve_id}'")
    return eleve


@router.post("/", response_model=EleveSchema, status_code=status.HTTP_201_CREATED)
async def create_eleve_endpoint(eleve_data: EleveSchema) -> EleveSchema:
    return await create_eleve(eleve_data)


@router.put("/{eleve_id}", response_model=EleveSchema, status_code=status.HTTP_200_OK)
async def update_eleve_endpoint(eleve_id: str, eleve_data: UpdateEleveSchema) -> EleveSchema:
    if not ObjectId.is_valid(eleve_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    updated_eleve = await update_eleve(eleve_id, eleve_data)
    if not updated_eleve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No student with id '{eleve_id}'")
    return updated_eleve


@router.delete("/{eleve_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_eleve_endpoint(eleve_id: str) -> dict:
    if not ObjectId.is_valid(eleve_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    if not await delete_eleve(eleve_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No student with id '{eleve_id}'")
    return {"detail": "Student deleted"}
