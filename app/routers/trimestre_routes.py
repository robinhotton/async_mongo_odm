from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from ..schemas import TrimestreResponse, TrimestreCreate, TrimestreUpdate
from ..services import get_trimestre, get_trimestres, create_trimestre, update_trimestre, delete_trimestre


router = APIRouter(prefix="/trimestres", tags=["Trimestres"])


@router.get("/", response_model=List[TrimestreResponse], status_code=status.HTTP_200_OK)
async def read_trimestres() -> List[TrimestreResponse]:
    return await get_trimestres()


@router.get("/{trimestre_id}", response_model=TrimestreResponse, status_code=status.HTTP_200_OK)
async def read_trimestre(trimestre_id: str) -> TrimestreResponse:
    if not ObjectId.is_valid(trimestre_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    trimestre = await get_trimestre(ObjectId(trimestre_id))
    if not trimestre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No trimester with id '{trimestre_id}'")
    return trimestre


@router.post("/", response_model=TrimestreResponse, status_code=status.HTTP_201_CREATED)
async def create_trimestre_endpoint(trimestre_data: TrimestreCreate) -> TrimestreResponse:
    return await create_trimestre(trimestre_data)


@router.put("/{trimestre_id}", response_model=TrimestreResponse, status_code=status.HTTP_200_OK)
async def update_trimestre_endpoint(trimestre_id: str, trimestre_data: TrimestreUpdate) -> TrimestreResponse:
    if not ObjectId.is_valid(trimestre_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    updated_trimestre = await update_trimestre(ObjectId(trimestre_id), trimestre_data)
    if not updated_trimestre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No trimester with id '{trimestre_id}'")
    return updated_trimestre


@router.delete("/{trimestre_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_trimestre_endpoint(trimestre_id: str) -> dict:
    if not ObjectId.is_valid(trimestre_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    if not await delete_trimestre(ObjectId(trimestre_id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No trimester with id '{trimestre_id}'")
    return {"detail": "Trimester deleted"}