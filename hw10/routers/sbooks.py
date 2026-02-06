from fastapi import APIRouter, HTTPException, Depends
from hw10.schemas.sbooks import SbookResponseSchema, CreateSbookSchema, CreateSbookResponse
from hw10.dependencies import auth_dependency, cookie_dependency
from hw10.db.hw10_zoa_sbook_db import check_userid, get_sbooks_by_userid, create_new_bookid_db

router = APIRouter(prefix="", tags=["Бронирования авиаперелетов"])

@router.get('/sbooks/{user_id}', 
    summary='Получить список бронирований пользователя',
    response_model=list[SbookResponseSchema]
)
def get_sbook_list(user_id: int):
    username = check_userid(user_id)
    if username is None:
        raise HTTPException(status_code=404, detail=f'Пользователь с id = {user_id}, не найден!')
    return get_sbooks_by_userid(user_id)

@router.post('/sbooks', 
    summary='Добавить авиабронь',
    response_model=CreateSbookResponse
)
def create_new_bookid(sbook: CreateSbookSchema, dependency = Depends(cookie_dependency)):
    sbook_data = {
        'userid': sbook.userid,
        'carrid': sbook.carrid,
        'connid': sbook.connid,
        'fldate': sbook.fldate,
        'sflight_seats': sbook.sflight_seats
    }

    return create_new_bookid_db(sbook_data)

    


