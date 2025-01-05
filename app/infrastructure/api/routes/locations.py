from fastapi import APIRouter, Depends

from app.domain.entities.location import Location
from app.infrastructure.api.dependencies import get_location_repository
from app.usecases.location_usecases import CreateLocationUseCase

router = APIRouter()


@router.post("/locations/", response_model=Location)
async def create_location(
    location: Location,
    use_case: CreateLocationUseCase = Depends(
        lambda: CreateLocationUseCase(get_location_repository())
    ),
):
    return await use_case.execute(location)
