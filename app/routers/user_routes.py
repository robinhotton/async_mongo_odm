from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.security import ACCESS_TOKEN_EXPIRE_MINUTES, verify_password, create_access_token
from app.models.user import User
from app.schemas.user_schema import UserCreateSchema, UserUpdateSchema, UserSchema, TokenResponseSchema
from app.services.auth_service import authenticate_user, get_password_hash
from app.services.user_service import (
    create_user,
    get_user_by_email,
    get_user,
    update_user,
    delete_user
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=UserSchema)
async def signup(user_data: UserCreateSchema):
    existing_user = await get_user_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = await create_user(user_data)
    return user

@router.post("/login", response_model=TokenResponseSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data=user.dict(), expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/", response_model=List[UserSchema])
async def read_users():
    users = await User.find_all().to_list()
    return users

@router.get("/{user_id}", response_model=UserSchema)
async def read_user(user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserSchema)
async def update_user_endpoint(user_id: str, user_data: UserUpdateSchema):
    updated_user = await update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=dict)
async def delete_user_endpoint(user_id: str):
    if not await delete_user(user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"detail": "User deleted"}
