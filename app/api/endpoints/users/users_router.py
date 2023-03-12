from fastapi import APIRouter

from app.api.endpoints.users.users_service import UsersService

router = APIRouter()
_users_service = UsersService()


@router.get("/users/")
def get_users() -> UsersService.GetUsersRes:
    users = _users_service.get_users()
    return users
