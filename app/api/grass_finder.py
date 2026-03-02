from fastapi import APIRouter

import random

router = APIRouter(prefix="/grass-finder", tags=["grass"])

GRASS_DATABASE = [
    {"plant": "Wood Sorrel", "location": "Behind Starry Live House", "flavor": "Citrusy, high acidity"},
    {"plant": "Dandelion Greens", "location": "Shimokitazawa Park", "flavor": "Bitter, like our last ticket sales"},
    {"plant": "Common Clover", "location": "Under the Chuo Line tracks", "flavor": "Earthy, slightly crunchy"},
    {"plant": "Moss", "location": "Nijika's backyard (sneaky)", "flavor": "Tastes like damp regret"}
]

@router.get("/find")
async def get_grass():
    recommendation = random.choice(GRASS_DATABASE)
    return {
        "ryo_says": "Life is hard, but the grass is free.",
        "intel": recommendation
    }

@router.get("/mood")
async def ryo_mood():
    moods = ["Thinking about bass lines", "Starving", "Ascending", "Ignoring Nijika's texts"]
    return {"status": random.choice(moods)}