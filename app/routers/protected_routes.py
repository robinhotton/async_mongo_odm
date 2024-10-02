from fastapi import APIRouter, Depends
from ..services.auth_service import check_role, get_current_user
from ..models import User
from ..enums import RoleEnum


router = APIRouter(prefix="/protected", tags=["Protected"])


@router.get("/admin-only", dependencies=[Depends(check_role(RoleEnum.ADMIN))])
async def admin_only_route(current_user: User = Depends(get_current_user)):
    return {"message": "Welcome, Admin!", "username": current_user.username, "roles": current_user.roles}


@router.get("/user-info")
async def user_info(current_user: User = Depends(get_current_user)):
    return {"message": "Welcome User", "username": current_user.username, "roles": current_user.roles}
