from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.profile_schema import ProfileSchema, UpdateProfileSchema
from app.services.profile_service import (
    get_profile,
    get_profiles,
    create_profile,
    update_profile,
    delete_profile,
)

router = APIRouter()

@router.get("/profiles/", response_model=List[ProfileSchema])
async def read_profiles():
    return await get_profiles()

@router.get("/profiles/{profile_id}", response_model=ProfileSchema)
async def read_profile(profile_id: str):
    profile = await get_profile(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"No profile with id '{profile_id}'")
    return profile

@router.post("/profiles/", response_model=ProfileSchema)
async def create_profile_endpoint(profile_data: ProfileSchema):
    return await create_profile(profile_data)

@router.put("/profiles/{profile_id}", response_model=ProfileSchema)
async def update_profile_endpoint(profile_id: str, profile_data: UpdateProfileSchema):
    updated_profile = await update_profile(profile_id, profile_data)
    if not updated_profile:
        raise HTTPException(status_code=404, detail=f"No profile with id '{profile_id}'")
    return updated_profile

@router.delete("/profiles/{profile_id}", response_model=dict)
async def delete_profile_endpoint(profile_id: str):
    if not await delete_profile(profile_id):
        raise HTTPException(status_code=404, detail=f"No profile with id '{profile_id}'")
    return {"detail": "Profile deleted"}
