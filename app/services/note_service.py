from app.models.note import Notes
from app.schemas.note_schema import NoteSchema, UpdateNoteSchema
from typing import List, Optional

async def get_note(notes_id: int) -> Optional[Notes]:
    return await Notes.get(notes_id)

async def get_notes() -> List[Notes]:
    return await Notes.find_all().to_list()

async def create_note(notes_data: NoteSchema) -> Notes:
    notes = Notes(**notes_data.dict())
    await notes.insert()
    return notes

async def update_note(notes_id: int, notes_data: UpdateNoteSchema) -> Optional[Notes]:
    notes = await Notes.get(notes_id)
    if notes:
        update_data = notes_data.dict(exclude_unset=True)
        await notes.set(update_data)
        return notes
    return None

async def delete_note(notes_id: int) -> bool:
    notes = await Notes.get(notes_id)
    if notes:
        await notes.delete()
        return True
    return False
