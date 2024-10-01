from ..enums import RoleEnum
from ..models import User
from ..schemas import UserCreateSchema, UserUpdateSchema, UserResponseSchema
from typing import Optional
from bson import ObjectId
from ..utils import hash_password

async def create_user(user_data: UserCreateSchema) -> UserResponseSchema:
    # Hash the password
    hashed_password = hash_password(user_data.password)
    
    # Create the user document
    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password,  # Ensure hashed_password is included
        roles=[RoleEnum(role) for role in user_data.roles]  # Convert roles to RoleEnum
    )

    # Insert the user into the database
    await user.insert()

    # Return the created user
    # Return the created user
    return UserResponseSchema(
        id=str(user.id),
        username=user.username,
        email=user.email,
        roles=user.roles
    )

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
