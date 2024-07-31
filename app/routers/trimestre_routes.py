from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.trimestre_schema import TrimestreSchema, UpdateTrimestreSchema
from app.services.trimestre_service import (
    get_trimestre,
    get_trimestres,
    create_trimestre,
    update_trimestre,
    delete_trimestre,
)

router = APIRouter(prefix="/trimestres", tags=["Trimestres"])

@router.get("/", response_model=List[TrimestreSchema])
async def read_trimestres():
    return await get_trimestres()

@router.get("/{trimestre_id}", response_model=TrimestreSchema)
async def read_trimestre(trimestre_id: str):
    trimestre = await get_trimestre(trimestre_id)
    if not trimestre:
        raise HTTPException(status_code=404, detail=f"No trimester with id '{trimestre_id}'")
    return trimestre

@router.post("/", response_model=TrimestreSchema)
async def create_trimestre_endpoint(trimestre_data: TrimestreSchema):
    return await create_trimestre(trimestre_data)

@router.put("/{trimestre_id}", response_model=TrimestreSchema)
async def update_trimestre_endpoint(trimestre_id: str, trimestre_data: UpdateTrimestreSchema):
    updated_trimestre = await update_trimestre(trimestre_id, trimestre_data)
    if not updated_trimestre:
        raise HTTPException(status_code=404, detail=f"No trimester with id '{trimestre_id}'")
    return updated_trimestre

@router.delete("/{trimestre_id}", response_model=dict)
async def delete_trimestre_endpoint(trimestre_id: str):
    if not await delete_trimestre(trimestre_id):
        raise HTTPException(status_code=404, detail=f"No trimester with id '{trimestre_id}'")
    return {"detail": "Trimester deleted"}
