from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import Annotated

from faker import Faker
from fastapi import Depends, FastAPI, Query
from sqlmodel import select

from app.config import Settings, get_settings
from app.models import Category, Location, LocationCategoryReview
from app.utils.database import Session, create_db_and_tables, get_session

SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(_app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
fake = Faker()


@app.get("/health-check")
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "running": True,
        "environment": settings.environment,
        "testing": settings.testing,
    }


@app.get("/locations")
def get_locations(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Location]:
    locations = session.exec(select(Location).offset(offset).limit(limit)).all()
    return locations


@app.get("/categories")
def get_categories(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Category]:
    categories = session.exec(select(Category).offset(offset).limit(limit)).all()
    return categories


@app.get("/explorer/recommendations/")
def get_recommendations(
    session: SessionDep,
    limit: Annotated[int, Query(le=10)] = 10,
) -> list[LocationCategoryReview]:
    """
    Get 10 location-category combinations that need review, prioritizing those never reviewed
    and those not reviewed in the last 30 days.
    """

    # Subquery to get all reviewed combinations
    thirty_days_ago = datetime.now() - timedelta(days=30)

    never_reviewed = session.exec(
        select(LocationCategoryReview)
        .where(LocationCategoryReview.last_reviewed_at is None)
        .limit(limit)
    ).all()

    needs_review = session.exec(
        select(LocationCategoryReview)
        .where(LocationCategoryReview.last_reviewed_at < thirty_days_ago)
        .limit(limit)
    ).all()

    recommendations = never_reviewed + needs_review

    return recommendations[:limit]
