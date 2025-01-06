from pydantic import BaseModel


class LocationCategoryReview(BaseModel):
    id: str | None
    location_id: str
    category_id: str
    last_reviewed_at: str | None
