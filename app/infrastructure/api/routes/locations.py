from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.domain.entities.location import Location
from app.infrastructure.api.dependencies import get_location_repository
from app.usecases.location_usecases import CreateLocationUseCase, GetAllLocationsUseCase

router = APIRouter()


@router.post("/locations/", response_model=Location)
async def create_location(
    location: Location,
    use_case: CreateLocationUseCase = Depends(
        lambda: CreateLocationUseCase(get_location_repository())
    ),
):
    return await use_case.execute(location)


@router.get("/locations/")
async def get_locations(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    use_case: GetAllLocationsUseCase = Depends(
        lambda: GetAllLocationsUseCase(get_location_repository())
    ),
):
    return await use_case.execute(offset, limit)
