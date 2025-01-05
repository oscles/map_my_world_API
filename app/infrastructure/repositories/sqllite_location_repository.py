from datetime import datetime
from typing import Annotated, Optional
from uuid import uuid4

from fastapi import Query
from sqlmodel import Field, Session, SQLModel, select

from app.domain.entities.location import Location
from app.domain.repositories.location_repository import LocationRepository


class LocationModel(SQLModel, table=True):
    __tablename__ = "locations"

    id: str | None = Field(default=str(uuid4()), primary_key=True)
    latitude: str = Field(nullable=False)
    longitude: str = Field(nullable=False)
    name: str = Field(nullable=False, index=True)
    created_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))


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
