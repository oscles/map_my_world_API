from datetime import datetime
from typing import Optional

from sqlmodel import DateTime, Field, SQLModel


class LocationCategoryReview(SQLModel, table=True):
    __tablename__ = "location_category_reviewed"
    id: int | None = Field(default=None, primary_key=True)
    location_id: str = Field(foreign_key="locations.id")
    category_id: str = Field(foreign_key="categories.id")
    last_reviewed_at: Optional[datetime] = Field(DateTime, default=datetime.now)
