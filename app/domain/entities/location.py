from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class Location(BaseModel):
    id: UUID | None
    latitude: float = Field(..., description="Latitude of the location")
    longitude: float = Field(..., description="Longitude of the location")
    name: str = Field(..., description="Name of the location")
    created_at: datetime = Field(
        default_factory=datetime.now, description="Creation timestamp"
    )
