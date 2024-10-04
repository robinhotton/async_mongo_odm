from fastapi import APIRouter, status
from typing import List
from bson import ObjectId
from ..schemas import TrimestreResponse, TrimestreCreate, TrimestreUpdate
from ..services import get_trimestre, get_trimestres, create_trimestre, update_trimestre, delete_trimestre
from .routes_utils import _verify_object_id, _response_not_none


router_name = "trimestres"
router = APIRouter(prefix=f"/{router_name}", tags=[router_name.capitalize()])


@router.get("/", response_model=List[TrimestreResponse], status_code=status.HTTP_200_OK)
async def read_trimestres(skip: int = 0, limit: int = 100) -> List[TrimestreResponse]:
    trimestres: List[TrimestreResponse] = await get_trimestres(skip, limit)
    return trimestres


@router.get("/{trimestre_id}", response_model=TrimestreResponse, status_code=status.HTTP_200_OK)
async def read_trimestre(trimestre_id: str) -> TrimestreResponse:
    trimestre_id: ObjectId = _verify_object_id(trimestre_id)
    trimestre: TrimestreResponse = await get_trimestre(trimestre_id)
    _response_not_none(trimestre, trimestre_id, router.tags[0])
    return trimestre


@router.post("/", response_model=TrimestreResponse, status_code=status.HTTP_201_CREATED)
async def create_trimestre_endpoint(trimestre_data: TrimestreCreate) -> TrimestreResponse:
    trimestre: TrimestreResponse = await create_trimestre(trimestre_data)
    return trimestre


@router.put("/{trimestre_id}", response_model=TrimestreResponse, status_code=status.HTTP_200_OK)
async def update_trimestre_endpoint(trimestre_id: str, trimestre_data: TrimestreUpdate) -> TrimestreResponse:
    trimestre_id: ObjectId = _verify_object_id(trimestre_id)
    updated_trimestre: TrimestreResponse = await update_trimestre(trimestre_id, trimestre_data)
    _response_not_none(updated_trimestre, trimestre_id, router.tags[0])
    return updated_trimestre


@router.delete("/{trimestre_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_trimestre_endpoint(trimestre_id: str) -> dict:
    trimestre_id: ObjectId = _verify_object_id(trimestre_id)
    deleted_trimestre: bool = await delete_trimestre(trimestre_id)
    _response_not_none(deleted_trimestre, trimestre_id, router.tags[0])
    return {"message": f"Document with id '{trimestre_id}' deleted successfully"}