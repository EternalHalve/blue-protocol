from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import random
from database.connection import get_db
from database.crud import create_grass, update_grass, get_all_grass
from schemas.grass import GrassBase, GrassResponse, GrassUpdate
from database.models.grass_models import Grass

router = APIRouter(prefix="/grass-finder", tags=["grass"])

@router.post("/add", response_model=GrassResponse)
async def add_grass(grass: GrassBase, db: AsyncSession = Depends(get_db)):
    return await create_grass(db, grass)

@router.patch("/update", response_model=GrassResponse)
async def patch_grass(
    grass_id: int, 
    grass_update: GrassUpdate, 
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(select(Grass).filter(Grass.id == grass_id))
    db_grass = result.scalars().first()

    if not db_grass:
        raise HTTPException(status_code=404, detail="Grass not found")

    return await update_grass(db, db_grass, grass_update)

@router.get("/find")
async def get_grass(db: AsyncSession = Depends(get_db)):
    all_grass = await get_all_grass(db)
    
    if not all_grass:
        return {"ryo_says": "Even the grass is gone... I'm finished."}

    recommendation = random.choice(all_grass)
    
    return {
        "ryo_says": "Life is hard, but the grass is free.",
        "intel": {
            "id": recommendation.id,
            "plant": recommendation.plant,
            "location": recommendation.location,
            "flavor": recommendation.flavor
        }
    }

@router.get("/mood")
async def ryo_mood():
    moods = ["Thinking about bass lines", "Starving", "Ascending", "Ignoring Nijika's texts"]
    return {"status": random.choice(moods)}