from app.domain.entities.location import Location
from app.domain.repositories.location_repository import LocationRepository


class CreateLocationUseCase:
    def __init__(self, location_repository: LocationRepository):
        self.location_repository = location_repository

    async def execute(self, location_data: Location) -> Location:
        return await self.location_repository.create(location_data)


class GetAllLocationsUseCase:
    def __init__(self, location_repository: LocationRepository):
        self.location_repository = location_repository

    async def execute(self) -> Location:
        return await self.location_repository.all()
