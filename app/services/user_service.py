from app.models.user import User
from app.schemas.user_schema import UserCreateSchema, UserUpdateSchema
from typing import Optional
from bson import ObjectId
from app.utils.security import hash_password

async def create_user(user_data: UserCreateSchema) -> User:
    user_data.password = hash_password(user_data.password)
    user = User(**user_data.dict())
    await user.insert()
    return user

async def get_user_by_email(email: str) -> Optional[User]:
    return await User.find_one(User.email == email)

async def get_user(user_id: str) -> Optional[User]:
    return await User.get(ObjectId(user_id))

async def update_user(user_id: str, user_data: UserUpdateSchema) -> Optional[User]:
    user = await User.get(ObjectId(user_id))
    if user:
        update_data = user_data.dict(exclude_unset=True)
        if "password" in update_data:
            update_data["password"] = hash_password(update_data["password"])
        await user.set(update_data)
        return user
    return None

async def delete_user(user_id: str) -> bool:
    user = await User.get(ObjectId(user_id))
    if user:
        await user.delete()
        return True
    return False
