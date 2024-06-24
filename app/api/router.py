from fastapi import APIRouter

from app.api.endpoints.files import files_router
from app.api.endpoints.users import users_router

api_router = APIRouter()
api_router.include_router(users_router.router, tags=["users"])
api_router.include_router(files_router.router, tags=["files"])
