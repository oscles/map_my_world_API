from dataclasses import dataclass
from datetime import datetime


@dataclass
class LocationCategoryReview:
    id: int | None
    location_id: int
    category_id: int
    last_reviewed_at: datetime
