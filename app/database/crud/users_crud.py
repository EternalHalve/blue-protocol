from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models.users import User
from schemas.users import UserCreate
from core.security import get_pass_hash


async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()


async def create_user(db: AsyncSession, user_in: UserCreate):
    hashed_password = get_pass_hash(user_in.password)
    db_user = User(
        username=user_in.username, email=user_in.email, hashed_password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def delete_user(db: AsyncSession, db_user: User) -> None:
    await db.delete(db_user)
    await db.commit()


async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()
