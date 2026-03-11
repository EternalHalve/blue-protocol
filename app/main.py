from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import grass_finder, auth, user
from core.config import CONFIG
from database.connection import engine, AsyncSessionLocal
from database.crud.grass_crud import seed_grass
from database.base import Base


@asynccontextmanager
async def lifespan(_app: FastAPI):
    if not CONFIG.SECRET_KEY:
        raise ValueError("Security Breach: SECRET_KEY is not set in the configuration.")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        await seed_grass(session)
    yield


app = FastAPI(
    title=CONFIG.PROJECT_NAME,
    version=CONFIG.PROJECT_VERSION,
    description="Grass Finder API",
    lifespan=lifespan,
)


@app.get("/")
async def main():
    return {"message": "Goodbye, World."}


app.include_router(grass_finder.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(user.router, prefix="/api")
