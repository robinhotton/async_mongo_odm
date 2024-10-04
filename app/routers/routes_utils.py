from fastapi import HTTPException, status
from pydantic import BaseModel
from bson import ObjectId   


def _verify_object_id(object_id: str) -> ObjectId:
    if not ObjectId.is_valid(object_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    return ObjectId(object_id)


def _response_not_none(response: BaseModel, classe_id: ObjectId, collection_name: str) -> None:
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No document with id '{classe_id}' in collection '{collection_name}'")