from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlmodel import Field, SQLModel


class LocationCategoryReview(SQLModel, table=True):
    __tablename__ = "location_category_reviewed"
    id: str | None = Field(default=str(uuid4()), primary_key=True)
    location_id: str = Field(foreign_key="locations.id")
    category_id: str = Field(foreign_key="categories.id")
    last_reviewed_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))
