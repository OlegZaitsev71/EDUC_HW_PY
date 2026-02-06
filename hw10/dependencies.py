from fastapi import HTTPException, Cookie
from typing import Optional
from hw10.auth import security

async def get_token_from_cookies(access_token: Optional[str] = Cookie(None, alias="access_token")) -> str:
    if not access_token:
        raise HTTPException(status_code=401, detail="Token missing")
    return access_token

# Общие зависимости для защиты эндпоинтов
auth_dependency = security.access_token_required
cookie_dependency = get_token_from_cookies