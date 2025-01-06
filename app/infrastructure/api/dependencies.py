from app.infrastructure.database import get_session
from app.infrastructure.repositories.sqllite_category_repository import (
    SQLLiteCategoryRepository,
)
from app.infrastructure.repositories.sqllite_location_repository import (
    SQLLiteLocationRepository,
)
from app.infrastructure.repositories.sqllite_review_repository import (
    SQLLiteLocationCategoryReviewRepository,
)


def get_location_repository():
    return SQLLiteLocationRepository(next(get_session()))


def get_category_repository():
    return SQLLiteCategoryRepository(next(get_session()))


def get_review_repository():
    return SQLLiteLocationCategoryReviewRepository(next(get_session()))
