from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from database.connection import get_db
from schemas.users import UserCreate, UserResponse, Token
from database.crud.users_crud import get_user_by_username, create_user
from core.security import verify_pass, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def register_user(
    user_create: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]
):
    existing_user = await get_user_by_username(db, user_create.username)
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Mainstream Username: Username already registered."
        )

    return await create_user(db, user_create)


@router.post("/login", response_model=Token)
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> Token:
    user = await get_user_by_username(db, form_data.username)

    if not user or not verify_pass(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access Denied: Invalid identification or passcode.",
        )

    access_token = create_access_token(data={"sub": str(user.id)})

    return Token(access_token=access_token, token_type="bearer")
