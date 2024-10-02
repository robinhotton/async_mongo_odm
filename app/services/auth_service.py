from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
import jwt  # PyJWT
from ..models import User
from ..utils import settings

# Create a password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define OAuth2PasswordBearer to be used in the dependency injection
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Verify plain password against hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Hash a plain password
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# Authenticate user by username and password
async def authenticate_user(username: str, password: str) -> Optional[User]:
    # Retrieve user from database by username
    user = await User.find_one({"username": username})

    # If the user does not exist or the password is incorrect, return None
    if not user or not verify_password(password, user.hashed_password):
        return None

    return user


# Retrieve current user based on the JWT token
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        # Decode the JWT token using SECRET_KEY and ALGORITHM
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        # Extract the username from the token's payload
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

        # Retrieve user from the database by username
        user = await User.find_one({"username": username})

        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

        return user

    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


# Role checking middleware to verify user roles
def check_role(required_role: str):
    async def role_checker(user: User = Depends(get_current_user)):
        # If the user does not have the required role, raise a 403 Forbidden error
        if required_role not in user.roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
        return user

    return role_checker


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()

    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt
