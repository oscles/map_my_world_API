from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Category:
    id: UUID | None
    name: str
    description: str | None
    created_at: datetime | None = None
