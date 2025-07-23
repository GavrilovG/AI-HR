from fastapi import Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from passlib.context import CryptContext

from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from ...core.services import UserRepository
from ...core.modules.user.dto import UserDto
from ...core.modules.user.filters import UserFilterDto
from ...settings import AuthSettings, get_settings
from src.core.modules.user.queries import GetUserQuery

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=10)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, get_settings(AuthSettings).secret_key, algorithm=get_settings(AuthSettings).algorithm)
    return encode_jwt


def get_hash(password: str) -> str:
    return pwd_context.hash(password)

async def authenticate_user(email: str, password: str):
    user = await UserRepository().get_user(UserFilterDto(email=email))
    if user is None or not pwd_context.verify(password, user.password):
        return None
    return user

def get_token(request: Request):
    token = request.cookies.get('users_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Войдите еще раз')
    return token

async def get_current_user(token: str = Depends(get_token)) -> UserDto:
    try:
        payload = jwt.decode(token, get_settings(AuthSettings).secret_key, algorithms=[get_settings(AuthSettings).algorithm])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Войдите еще раз')

    expire = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
    if (not expire) or (expire_time < datetime.now(timezone.utc)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Войдите еще раз')
    user_id = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Войдите еще раз')
    user = await GetUserQuery(id=int(user_id))
    return user