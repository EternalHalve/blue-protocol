from pydantic import BaseModel, ConfigDict
from typing import Optional

class GrassBase(BaseModel):
    plant: str
    flavor: str
    location: str

class GrassUpdate(BaseModel):
    plant: Optional[str] = None
    flavor: Optional[str] = None
    location: Optional[str] = None

class GrassResponse(GrassBase):
    id: int

    model_config = ConfigDict(from_attributes=True)