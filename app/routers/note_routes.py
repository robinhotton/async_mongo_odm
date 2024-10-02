from fastapi import APIRouter, HTTPException, status
from typing import List
from ..schemas import NoteSchema, UpdateNoteSchema
from ..services import get_notes, get_note, create_note, update_note, delete_note

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.get("/", response_model=List[NoteSchema])
async def read_notes():
    return await get_notes()

@router.get("/{note_id}", response_model=NoteSchema)
async def read_note(note_id: str):
    note = await get_note(note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No note with id '{note_id}'")
    return note

@router.post("/", response_model=NoteSchema)
async def create_note_endpoint(note_data: NoteSchema):
    return await create_note(note_data)

@router.put("/{note_id}", response_model=NoteSchema)
async def update_note_endpoint(note_id: str, note_data: UpdateNoteSchema):
    updated_note = await update_note(note_id, note_data)
    if not updated_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No note with id '{note_id}'")
    return updated_note

@router.delete("/{note_id}", response_model=dict)
async def delete_note_endpoint(note_id: str):
    if not await delete_note(note_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No note with id '{note_id}'")
    return {"detail": "Note deleted"}
