from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from random import random, choice

from core.config import CONFIG
from database.connection import get_db
from database.crud.users_crud import get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Security Breach: Could not validate credentials. Re-authenticate or remain hungry.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, CONFIG.SECRET_KEY, algorithms=[CONFIG.ALGORITHM])
        user_id: str = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except jwt.PyJWTError:
        raise credentials_exception

    user = await get_user_by_id(db, user_id=int(user_id))
    if user is None:
        raise credentials_exception

    return user


async def ryo_mood_guard():
    if random() < 0.1:
        moods = [
            {
                "status": status.HTTP_503_SERVICE_UNAVAILABLE,
                "msg": "Go away. I'm busy ignoring people.",
            },
            {
                "status": status.HTTP_402_PAYMENT_REQUIRED,
                "msg": "I spent all my money on a bass. Buy me curry?",
            },
            {
                "status": status.HTTP_418_IM_A_TEAPOT,
                "msg": "I'm currently a blade of grass. Do not disturb.",
            },
            {
                "status": status.HTTP_404_NOT_FOUND,
                "msg": "I've wandered into a shady instrument shop. Try again later.",
            },
        ]

        bad_mood = choice(moods)

        raise HTTPException(
            status_code=bad_mood["status"],
            detail={
                "ryo_says": bad_mood["msg"],
                "system_status": "RYO_UNAVAILABLE_ERROR",
            },
        )

    return "Neutral"
