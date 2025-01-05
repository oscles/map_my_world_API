from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field as FieldPD
from sqlmodel import Field, SQLModel


class Location(SQLModel, table=True):
    __tablename__ = "locations"

    id: str | None = Field(default=str(uuid4()), primary_key=True)
    latitude: str = Field(nullable=False)
    longitude: str = Field(nullable=False)
    name: str = Field(nullable=False, index=True)
    created_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))


class CreateLocationDto(BaseModel):
    latitude: float = FieldPD(..., description="Latitude of the location")
    longitude: float = FieldPD(..., description="Longitude of the location")
    name: str = FieldPD(..., description="Name of the location")
