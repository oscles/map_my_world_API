from typing import Annotated

from fastapi import Query
from sqlmodel import Session, select

from app.domain.entities.location import Location
from app.domain.repositories.location_repository import LocationRepository
from app.infrastructure.models.models import LocationModel


class SQLLiteLocationRepository(LocationRepository):
    def __init__(self, session: Session):
        self.session = session

    async def create(self, location: Location) -> Location:
        db_location = LocationModel(
            latitude=location.latitude, longitude=location.longitude, name=location.name
        )

        self.session.add(db_location)
        self.session.commit()
        self.session.refresh(db_location)

        return Location(
            id=db_location.id,
            latitude=db_location.latitude,
            longitude=db_location.longitude,
            name=db_location.name,
            created_at=db_location.created_at,
        )

    async def all(
        self,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
    ):
        locations = self.session.exec(
            select(LocationModel).offset(offset).limit(limit)
        ).all()

        return locations
