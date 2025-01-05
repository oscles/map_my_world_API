from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Location:
    id: UUID | None
    latitude: float
    longitude: float
    name: str
    created_at: datetime | None = None
