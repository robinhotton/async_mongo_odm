from app.models.profile import Profile
from app.schemas.profile_schema import ProfileSchema, UpdateProfileSchema
from typing import List, Optional
from bson import ObjectId

async def get_profile(profile_id: str) -> Optional[Profile]:
    return await Profile.get(profile_id)

async def get_profiles() -> List[Profile]:
    return await Profile.find_all().to_list()

async def create_profile(profile_data: ProfileSchema) -> Profile:
    profile = Profile(**profile_data.dict())
    await profile.insert()
    return profile

async def update_profile(profile_id: str, profile_data: UpdateProfileSchema) -> Optional[Profile]:
    profile = await Profile.get(profile_id)
    if profile:
        update_data = profile_data.dict(exclude_unset=True)
        await profile.set(update_data)
        return profile
    return None

async def delete_profile(profile_id: str) -> bool:
    profile = await Profile.get(profile_id)
    if profile:
        await profile.delete()
        return True
    return False
