from fastapi import APIRouter, status
from typing import List
from bson import ObjectId
from ..schemas import ProfesseurResponse, ProfesseurCreate, ProfesseurUpdate
from ..services import get_professeur, get_professeurs, create_professeur, update_professeur, delete_professeur
from .routes_utils import _verify_object_id, _response_not_none


router_name = "professeurs"
router = APIRouter(prefix=f"/{router_name}", tags=[router_name.capitalize()])


@router.get("/", response_model=List[ProfesseurResponse], status_code=status.HTTP_200_OK)
async def read_professeurs(skip: int = 0, limit: int = 100) -> List[ProfesseurResponse]:
    professeurs: List[ProfesseurResponse] = await get_professeurs(skip, limit)
    return professeurs


@router.get("/{professeur_id}", response_model=ProfesseurResponse, status_code=status.HTTP_200_OK)
async def read_professeur(professeur_id: str) -> ProfesseurResponse:
    professeur_id: ObjectId = _verify_object_id(professeur_id)
    professeur: ProfesseurResponse = await get_professeur(professeur_id)
    _response_not_none(professeur, professeur_id, router_name)
    return professeur


@router.post("/", response_model=ProfesseurResponse, status_code=status.HTTP_201_CREATED)
async def create_professeur_endpoint(professeur_data: ProfesseurCreate) -> ProfesseurResponse:
    professeur: ProfesseurResponse = await create_professeur(professeur_data)
    return professeur


@router.put("/{professeur_id}", response_model=ProfesseurResponse, status_code=status.HTTP_200_OK)
async def update_professeur_endpoint(professeur_id: str, professeur_data: ProfesseurUpdate) -> ProfesseurResponse:
    professeur_id: ObjectId = _verify_object_id(professeur_id)
    updated_professeur: ProfesseurResponse = await update_professeur(professeur_id, professeur_data)
    _response_not_none(updated_professeur, professeur_id, router_name)
    return updated_professeur


@router.delete("/{professeur_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_professeur_endpoint(professeur_id: str) -> dict:
    professeur_id: ObjectId = _verify_object_id(professeur_id)
    deleted_professeur: bool = await delete_professeur(professeur_id)
    _response_not_none(deleted_professeur, professeur_id, router_name)
    return {"message": f"Document with id '{professeur_id}' deleted successfully"}