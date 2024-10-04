from fastapi import APIRouter, status
from typing import List
from bson import ObjectId
from ..schemas import MatiereResponse, MatiereCreate, MatiereUpdate
from ..services import get_matiere, get_matieres, create_matiere, update_matiere, delete_matiere
from .routes_utils import _verify_object_id, _response_not_none


router_name = "matieres"
router = APIRouter(prefix=f"/{router_name}", tags=[router_name.capitalize()])


@router.get("/", response_model=List[MatiereResponse], status_code=status.HTTP_200_OK)
async def read_matieres(skip: int = 0, limit: int = 100) -> List[MatiereResponse]:
    matieres: List[MatiereResponse] = await get_matieres(skip, limit)
    return matieres


@router.get("/{matiere_id}", response_model=MatiereResponse, status_code=status.HTTP_200_OK)
async def read_matiere(matiere_id: str) -> MatiereResponse:
    matiere_id: ObjectId = _verify_object_id(matiere_id)
    matiere: MatiereResponse = await get_matiere(matiere_id)
    _response_not_none(matiere, matiere_id, router_name)
    return matiere


@router.post("/", response_model=MatiereResponse, status_code=status.HTTP_201_CREATED)
async def create_matiere_endpoint(matiere_data: MatiereCreate) -> MatiereResponse:
    matiere: MatiereResponse = await create_matiere(matiere_data)
    return matiere


@router.put("/{matiere_id}", response_model=MatiereResponse, status_code=status.HTTP_200_OK)
async def update_matiere_endpoint(matiere_id: str, matiere_data: MatiereUpdate) -> MatiereResponse:
    matiere_id: ObjectId = _verify_object_id(matiere_id)
    updated_matiere: MatiereResponse = await update_matiere(matiere_id, matiere_data)
    _response_not_none(updated_matiere, matiere_id, router_name)
    return updated_matiere


@router.delete("/{matiere_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_matiere_endpoint(matiere_id: str) -> dict:
    matiere_id: ObjectId = _verify_object_id(matiere_id)
    deleted_matiere: bool = await delete_matiere(matiere_id)
    _response_not_none(deleted_matiere, matiere_id, router_name)
    return {"message": f"Document with id '{matiere_id}' deleted successfully"}