from dataclasses import dataclass
from datetime import datetime


@dataclass
class Location:
    id: int | None
    latitude: float
    longitude: float
    name: str
    created_at: datetime | None = None
