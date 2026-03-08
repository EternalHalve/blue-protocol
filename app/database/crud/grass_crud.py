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

    db.add(db_grass)
    await db.commit()
    await db.refresh(db_grass)


async def delete_grass(db: AsyncSession, db_grass: Grass) -> Grass:
    await db.delete(db_grass)
    await db.commit()
    return True


async def seed_grass(db: AsyncSession):
    result = await db.execute(select(Grass))
    if not result.scalars().first():
        initial_grass = [
            Grass(
                plant="Wood Sorrel",
                location="Behind Starry Live House",
                flavor="Citrusy, high acidity",
            ),
            Grass(
                plant="Dandelion Greens",
                location="Shimokitazawa Park",
                flavor="Bitter, like our last ticket sales",
            ),
            Grass(
                plant="Common Clover",
                location="Under the Chuo Line tracks",
                flavor="Earthy, slightly crunchy",
            ),
            Grass(
                plant="Moss",
                location="Nijika's backyard (sneaky)",
                flavor="Tastes like damp regret",
            ),
        ]
        db.add_all(initial_grass)
        await db.commit()
        print("Database seeded: Ryo's secret menu added!")


async def get_all_grass(db: AsyncSession):
    result = await db.execute(select(Grass))
    return result.scalars().all()