from fastapi import APIRouter, HTTPException, Response
from hw10.schemas.users import UserLoginSchema
from hw10.auth import security, config

router = APIRouter(prefix="", tags=["Аутентификация"])

@router.post('/login', summary='Аутентификация пользователя')
def login(credentials: UserLoginSchema, response: Response):
    if credentials.user_name == 'admin1' and credentials.password == '321':
        token = security.create_access_token(uid='654321')
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {'access_token': token}
    
    raise HTTPException(status_code=401, detail='Incorrect username or password')