from fastapi import APIRouter, status
from typing import List
from bson import ObjectId
from ..schemas import EleveResponse, EleveCreate, EleveUpdate
from ..services import get_eleve, get_eleves, create_eleve, update_eleve, delete_eleve
from .routes_utils import _verify_object_id, _response_not_none


route_name = "eleves"
router = APIRouter(prefix=f"/{route_name}", tags=[route_name.capitalize()])


@router.get("/", response_model=List[EleveResponse], status_code=status.HTTP_200_OK)
async def read_eleves(skip: int = 0, limit: int = 100) -> List[EleveResponse]:
    eleves: List[EleveResponse] = await get_eleves(skip, limit)
    return eleves


@router.get("/{eleve_id}", response_model=EleveResponse, status_code=status.HTTP_200_OK)
async def read_eleve(eleve_id: str) -> EleveResponse:
    eleve_id: ObjectId = _verify_object_id(eleve_id)
    eleve: EleveResponse = await get_eleve(eleve_id)
    _response_not_none(eleve, eleve_id, route_name)
    return eleve


@router.post("/", response_model=EleveResponse, status_code=status.HTTP_201_CREATED)
async def create_eleve_endpoint(eleve_data: EleveCreate) -> EleveResponse:
    eleve: EleveResponse = await create_eleve(eleve_data)
    return eleve


@router.put("/{eleve_id}", response_model=EleveResponse, status_code=status.HTTP_200_OK)
async def update_eleve_endpoint(eleve_id: str, eleve_data: EleveUpdate) -> EleveResponse:
    eleve_id: ObjectId = _verify_object_id(eleve_id)    
    updated_eleve: EleveResponse = await update_eleve(eleve_id, eleve_data)
    _response_not_none(updated_eleve, eleve_id, route_name)
    return updated_eleve


@router.delete("/{eleve_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_eleve_endpoint(eleve_id: str) -> dict:
    eleve_id: ObjectId = _verify_object_id(eleve_id)
    deleted_eleve: bool = await delete_eleve(eleve_id)
    _response_not_none(deleted_eleve, eleve_id, route_name)
    return {"message": f"Document with id '{eleve_id}' deleted successfully"}