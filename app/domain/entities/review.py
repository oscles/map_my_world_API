from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class LocationCategoryReview:
    id: UUID | None
    location_id: int
    category_id: int
    last_reviewed_at: Optional[datetime] = None
