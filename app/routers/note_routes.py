from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from typing import List
from ..schemas import NoteResponse, NoteCreate, NoteUpdate
from ..services import get_notes, get_note, create_note, update_note, delete_note


router = APIRouter(prefix="/notes", tags=["Notes"])


@router.get("/", response_model=List[NoteResponse], status_code=status.HTTP_200_OK)
async def read_notes() -> List[NoteResponse]:
    return await get_notes()


@router.get("/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
async def read_note(note_id: str) -> NoteResponse:
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    note = await get_note(ObjectId(note_id))
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No note with id '{note_id}'")
    return note


@router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
async def create_note_endpoint(note_data: NoteCreate) -> NoteResponse:
    return await create_note(note_data)


@router.put("/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
async def update_note_endpoint(note_id: str, note_data: NoteUpdate) -> NoteResponse:
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    updated_note = await update_note(ObjectId(note_id), note_data)
    if not updated_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No note with id '{note_id}'")
    return updated_note


@router.delete("/{note_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_note_endpoint(note_id: str) -> dict:
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    if not await delete_note(ObjectId(note_id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No note with id '{note_id}'")
    return {"detail": "Note deleted"}