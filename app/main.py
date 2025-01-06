from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from app.config import Settings, get_settings
from app.infrastructure.api.routes import category, locations, review
from app.utils.database import create_db_and_tables


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


@app.get("/health-check")
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "running": True,
        "environment": settings.environment,
        "testing": settings.testing,
    }


app.include_router(locations.router, tags=["Locations"])
app.include_router(category.router, tags=["Categories"])
app.include_router(review.router, tags=["Recommendations"])
