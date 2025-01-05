import math
from uuid import uuid4

from app.domain.entities.category import Category
from app.domain.entities.location import Location
from app.models.review import LocationCategoryReview


def test_location_creation():
    location = Location(
        id=uuid4(), latitude=40.7128, longitude=-74.0060, name="New York City"
    )

    assert math.isclose(location.latitude, 40.7128, rel_tol=1e-9)
    assert location.longitude == -74.0060
    assert location.name == "New York City"
    assert location.id


def test_category_creation():
    category = Category(id=uuid4(), name="Restaurant", description="Places to eat")

    assert category.name == "Restaurant"
    assert category.description == "Places to eat"
    assert category.id


def test_location_category_review_creation():
    location = Location(
        id=uuid4(), latitude=40.7128, longitude=-74.0060, name="New York City"
    )
    category = Category(id=uuid4(), name="Restaurant", description="Places to eat")
    review = LocationCategoryReview(
        id=uuid4(),
        location_id=location.id,
        category_id=category.id,
        last_reviewed_at=None,
    )

    assert review.id
    assert review.category_id == category.id
    assert review.location_id == location.id
    assert review.last_reviewed_at is None
