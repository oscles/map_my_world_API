from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from sqlmodel import Field, Relationship, SQLModel


class LocationCategoryReviewModel(SQLModel, table=True):
    __tablename__ = "location_category_reviewed"

    id: str = Field(primary_key=True, index=True, unique=True)
    location_id: str = Field(foreign_key="locations.id")
    category_id: str = Field(foreign_key="categories.id")
    last_reviewed_at: Optional[str] = Field(default=None, nullable=True)

    # Relationships
    location: "LocationModel" = Relationship(back_populates="reviews")
    category: "CategoryModel" = Relationship(back_populates="reviews")


class LocationModel(SQLModel, table=True):
    __tablename__ = "locations"

    id: str | None = Field(
        default_factory=lambda: str(uuid4()), primary_key=True, index=True, unique=True
    )
    latitude: str = Field(nullable=False)
    longitude: str = Field(nullable=False)
    name: str = Field(nullable=False, index=True)
    created_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))

    # Relationship
    reviews: List[LocationCategoryReviewModel] = Relationship(back_populates="location")


class CategoryModel(SQLModel, table=True):
    __tablename__ = "categories"

    id: str | None = Field(
        default_factory=lambda: str(uuid4()), primary_key=True, index=True, unique=True
    )
    name: str = Field(unique=True, nullable=False, index=True)
    description: str = Field(nullable=False)
    created_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))

    # Relationship
    reviews: List[LocationCategoryReviewModel] = Relationship(back_populates="category")


class ReviewResponse(SQLModel):
    id: str
    last_reviewed_at: Optional[str]
    location: LocationModel
    category: CategoryModel

    class Config:
        from_attributes = True
