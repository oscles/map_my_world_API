from typing import List

from app.domain.entities.review import LocationCategoryReview
from app.domain.repositories.review_repository import LocationCategoryReviewRepository


class GetRecommendationsUseCase:
    def __init__(self, review_repository: LocationCategoryReviewRepository):
        self.review_repository = review_repository

    async def execute(self, limit: int = 10) -> List[LocationCategoryReview]:
        return await self.review_repository.get_recommendations(limit)
