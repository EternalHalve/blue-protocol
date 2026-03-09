from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schemas.grass import GrassBase, GrassUpdate
from database.models.grass_models import Grass


async def create_grass(db: AsyncSession, grass_create: GrassBase) -> Grass:
    grass_data = grass_create.model_dump()
    new_grass = Grass(**grass_data)

    db.add(new_grass)
    await db.commit()
    await db.refresh(new_grass)

    return new_grass


async def update_grass(
    db: AsyncSession, db_grass: Grass, grass_update: GrassUpdate
) -> Grass:
    update_data = grass_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_grass, key, value)

    await db.commit()
    await db.refresh(db_grass)
    return db_grass


async def delete_grass(db: AsyncSession, db_grass: Grass) -> Grass:
    await db.delete(db_grass)
    await db.commit()
    return True


async def seed_grass(db: AsyncSession):
    result = await db.execute(select(Grass))
    if not result.scalars().first():
        initial_grass = [
            Grass(
                plant="Wood Sorrel (Oxalis)",
                location="Damp, shaded cracks in concrete retaining walls",
                flavor="Sharp, oxalic sting; like a lemon-scented battery.",
            ),
            Grass(
                plant="Hairy Bittercress",
                location="Neglected gravel driveways and nursery pots",
                flavor="Peppery and explosive; the crunch of desperate microgreens.",
            ),
            Grass(
                plant="Japanese Knotweed (Shoots)",
                location="Riverbanks and disturbed soil near railway embankments",
                flavor="Sour and crunchy; tastes like a rhubarb heist.",
            ),
            Grass(
                plant="Mugwort (Artemisia)",
                location="Dry roadsides and abandoned industrial lots",
                flavor="Bitter and aromatic; the flavor of a tea you can't afford.",
            ),
            Grass(
                plant="Common Chickweed",
                location="Moist garden paths and nitrogen-rich waste ground",
                flavor="Cool and grassy; like eating a salad in a cemetery.",
            ),
        ]
        db.add_all(initial_grass)
        await db.commit()
        print("Database seeded: Ryo's secret menu added.")


async def get_grass(db: AsyncSession, grass_id: int) -> Grass | None:
    return await db.get(Grass, grass_id)


async def get_random_grass(db: AsyncSession) -> Grass | None:
    query = select(Grass).order_by(func.random()).limit(1)
    result = await db.execute(query)
    return result.scalars().first()
