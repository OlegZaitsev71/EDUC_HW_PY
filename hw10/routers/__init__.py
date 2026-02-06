from fastapi import APIRouter

from hw10.routers.auth import router as auth_router
from hw10.routers.users import router as user_router
from hw10.routers.sbooks import router as sbook_router

main_router = APIRouter()

main_router.include_router(auth_router, tags=["Аутентификация"])
main_router.include_router(user_router, tags=["Пользователи"])
main_router.include_router(sbook_router, tags=["Бронирования авиаперелетов"])