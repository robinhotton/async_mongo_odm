from typing import List, Optional
from bson import ObjectId
from ..models import Note
from ..schemas import NoteResponse, NoteCreate, NoteUpdate


async def get_notes() -> List[Note]:
    notes: List[Note] = await Note.find_all().to_list()
    response: List[NoteResponse] = [NoteResponse(_id=str(note.id), **note.model_dump()) for note in notes]
    return response


async def get_note(note_id: ObjectId) -> Optional[NoteResponse]:
    note: Note = await Note.get(note_id)
    response: NoteResponse = NoteResponse(_id=str(note.id), **note.model_dump())
    return response


async def create_note(note_data: NoteCreate) -> NoteResponse:
    note: Note = Note(**note_data.model_dump())
    await note.insert()
    response: NoteResponse = NoteResponse(_id=str(note.id), **note_data.model_dump())
    return response


async def update_note(note_id: ObjectId, note_data: NoteUpdate) -> Optional[NoteResponse]:
    note: Note = await Note.get(note_id)
    if note:
        update_data: NoteUpdate = note_data.model_dump(exclude_unset=True)
        await note.set(update_data)
        response: NoteResponse = NoteResponse(_id=str(note.id), **note.model_dump())
        return response
    return None


async def delete_note(note_id: ObjectId) -> bool:
    note: Note = await Note.get(note_id)
    if note:
        await note.delete()
        return True
    return False