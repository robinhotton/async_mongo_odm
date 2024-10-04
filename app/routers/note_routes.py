from fastapi import APIRouter, status
from typing import List
from bson import ObjectId
from ..schemas import NoteResponse, NoteCreate, NoteUpdate
from ..services import get_notes, get_note, create_note, update_note, delete_note
from .routes_utils import _verify_object_id, _response_not_none


router_name = "notes"
router = APIRouter(prefix=f"/{router_name}", tags=[router_name.capitalize()])


@router.get("/", response_model=List[NoteResponse], status_code=status.HTTP_200_OK)
async def read_notes(skip: int = 0, limit: int = 100) -> List[NoteResponse]:
    notes: List[NoteResponse] = await get_notes(skip, limit)
    return notes


@router.get("/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
async def read_note(note_id: str) -> NoteResponse:
    note_id: ObjectId = _verify_object_id(note_id)
    note: NoteResponse = await get_note(note_id)
    _response_not_none(note, note_id, router_name)
    return note


@router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
async def create_note_endpoint(note_data: NoteCreate) -> NoteResponse:
    note: NoteResponse = await create_note(note_data)
    return note


@router.put("/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
async def update_note_endpoint(note_id: str, note_data: NoteUpdate) -> NoteResponse:
    note_id: ObjectId = _verify_object_id(note_id)
    updated_note: NoteResponse = await update_note(note_id, note_data)
    _response_not_none(updated_note, note_id, router_name)
    return updated_note


@router.delete("/{note_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_note_endpoint(note_id: str) -> dict:
    note_id: ObjectId = _verify_object_id(note_id)
    deleted_note: bool = await delete_note(note_id)
    _response_not_none(deleted_note, note_id, router_name)
    return {"message": f"Document with id '{note_id}' deleted successfully"}