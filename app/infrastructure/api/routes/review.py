from typing import Annotated, List

from fastapi import APIRouter, Depends, Query

from app.infrastructure.api.dependencies import get_review_repository
from app.infrastructure.models.models import ReviewResponse
from app.usecases.review_usecase import GetRecommendationsUseCase

router = APIRouter()


@router.get("/recommendations/", response_model=List[ReviewResponse])
async def get_recommendations(
    limit: Annotated[int, Query(le=100)] = 100,
    use_case: GetRecommendationsUseCase = Depends(
        lambda: GetRecommendationsUseCase(get_review_repository())
    ),
):
    return await use_case.execute(limit)
