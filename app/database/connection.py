from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from core.config import CONFIG
from database.models.grass_models import Base

connect_args = {"check_same_thread": False} if "sqlite" in CONFIG.DB_URL else {}

engine = create_async_engine(CONFIG.DB_URL, connect_args=connect_args)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

async def init_models():
    engine = create_async_engine(CONFIG.DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

import asyncio
if __name__ == "__main__":
    asyncio.run(init_models())