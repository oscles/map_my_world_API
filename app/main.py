from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI

from app.config import Settings, get_settings
from app.infrastructure.api.routes import category, locations
from app.utils.database import Session, create_db_and_tables, get_session

SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(_app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Map My World API",
    description="API for managing locations, categories, and exploration recommendations",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(locations.router, tags=["Locations"])
app.include_router(category.router, tags=["Categories"])


@app.get("/health-check")
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "running": True,
        "environment": settings.environment,
        "testing": settings.testing,
    }


# @app.get("/explorer/recommendations/", tags=["Recommendations"])
# def get_recommendations(
#     session: SessionDep,
#     limit: Annotated[int, Query(le=10)] = 10,
# ) -> list[LocationCategoryReview]:
#     """
#     Get 10 location-category combinations that need review, prioritizing those never reviewed
#     and those not reviewed in the last 30 days.
#     """

#     # Subquery to get all reviewed combinations
#     thirty_days_ago = datetime.now() - timedelta(days=30)

#     never_reviewed = session.exec(
#         select(LocationCategoryReview)
#         .where(LocationCategoryReview.last_reviewed_at is None)
#         .limit(limit)
#     ).all()

#     needs_review = session.exec(
#         select(LocationCategoryReview)
#         .where(LocationCategoryReview.last_reviewed_at < thirty_days_ago)
#         .limit(limit)
#     ).all()

#     recommendations = never_reviewed + needs_review

#     return recommendations[:limit]
