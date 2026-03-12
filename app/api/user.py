from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps import get_current_user
from database.models.users import User
from database.connection import get_db
from database.crud.users_crud import delete_user, update_user
from schemas.users import UserResponse, DeleteAccountConfirmation, UserUpdate
from core.security import verify_pass

router = APIRouter(prefix="/users", tags=["user"])


@router.get("/me", response_model=UserResponse)
async def get_current_user_profile(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user

@router.patch("/me", response_model=UserResponse)
async def update_profile(
    user_update: UserUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
):
    updated_user = await update_user(db, current_user, user_update)
    return updated_user

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
    confirmation: DeleteAccountConfirmation,
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncSession = Depends(get_db),
):
    if not verify_pass(confirmation.password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Security Breach: Authentication key mismatch.",
        )

    if confirmation.confirm_text != "DELETE MY ACCOUNT":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Protocol Error: Manual override string must match 'DELETE MY ACCOUNT'.",
        )

    await delete_user(db, current_user)
    return None
