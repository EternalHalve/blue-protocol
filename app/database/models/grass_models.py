from sqlalchemy import String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class Grass(Base):
    __tablename__ = "grass_finder"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    plant: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    flavor: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)