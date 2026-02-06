from fastapi import APIRouter, HTTPException, Depends
from hw10.schemas.users import UserSchema, UserResponseSchema
from hw10.dependencies import auth_dependency, cookie_dependency
from hw10.db.hw10_zoa_sbook_db import get_users, get_user_by_id

router = APIRouter(prefix="", tags=["Пользователи"])

@router.get('/users', 
    summary='Получить список пользователей',
    response_model=list[UserResponseSchema]
)
def get_users_list(dependency = Depends(auth_dependency)):
    return get_users()

@router.get('/user/{user_id}',
    summary='Получить пользователя',
    response_model=UserResponseSchema
)
def get_user(user_id: int, dependency = Depends(auth_dependency)):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f'Пользователь с id = {user_id}, не найден!')
    return user

