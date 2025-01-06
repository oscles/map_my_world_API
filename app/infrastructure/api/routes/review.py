from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.infrastructure.api.dependencies import get_review_repository
from app.usecases.review_usecase import GetRecommendationsUseCase

router = APIRouter()


@router.get("/recommendations/")
async def get_recommendations(
    limit: Annotated[int, Query(le=10)] = 10,
    use_case: GetRecommendationsUseCase = Depends(
        lambda: GetRecommendationsUseCase(get_review_repository())
    ),
):
    return await use_case.execute(limit)
