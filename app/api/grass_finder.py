from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import random
from database.connection import get_db
from database.crud import create_grass, get_all_grass
from schemas.grass import GrassBase, GrassResponse

router = APIRouter(prefix="/grass-finder", tags=["grass"])

GRASS_DATABASE = [
    {"plant": "Wood Sorrel", "location": "Behind Starry Live House", "flavor": "Citrusy, high acidity"},
    {"plant": "Dandelion Greens", "location": "Shimokitazawa Park", "flavor": "Bitter, like our last ticket sales"},
    {"plant": "Common Clover", "location": "Under the Chuo Line tracks", "flavor": "Earthy, slightly crunchy"},
    {"plant": "Moss", "location": "Nijika's backyard (sneaky)", "flavor": "Tastes like damp regret"}
]

@router.post("/add", response_model=GrassResponse)
async def add_grass(grass: GrassBase, db: AsyncSession = Depends(get_db)):
    return await create_grass(db, grass)

@router.get("/find")
async def get_grass(db: AsyncSession = Depends(get_db)):
    all_grass = await get_all_grass(db)
    
    if not all_grass:
        return {"ryo_says": "Even the grass is gone... I'm finished."}

    recommendation = random.choice(all_grass)
    
    return {
        "ryo_says": "Life is hard, but the grass is free.",
        "intel": {
            "plant": recommendation.plant,
            "location": recommendation.location,
            "flavor": recommendation.flavor
        }
    }

@router.get("/mood")
async def ryo_mood():
    moods = ["Thinking about bass lines", "Starving", "Ascending", "Ignoring Nijika's texts"]
    return {"status": random.choice(moods)}