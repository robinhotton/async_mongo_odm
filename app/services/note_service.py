from app.models.note import Note
from app.schemas.note_schema import NoteSchema, UpdateNoteSchema
from typing import List, Optional

async def get_note(notes_id: int) -> Optional[Note]:
    return await Note.get(notes_id)

async def get_notes() -> List[Note]:
    return await Note.find_all().to_list()

async def create_note(notes_data: NoteSchema) -> Note:
    notes = Note(**notes_data.dict())
    await notes.insert()
    return notes

async def update_note(notes_id: int, notes_data: UpdateNoteSchema) -> Optional[Note]:
    notes = await Note.get(notes_id)
    if notes:
        update_data = notes_data.dict(exclude_unset=True)
        await notes.set(update_data)
        return notes
    return None

async def delete_note(notes_id: int) -> bool:
    notes = await Note.get(notes_id)
    if notes:
        await notes.delete()
        return True
    return False
