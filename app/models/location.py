from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlmodel import Field, SQLModel


class Location(SQLModel, table=True):
    __tablename__ = "locations"
    id: str | None = Field(default=str(uuid4()), primary_key=True)
    latitude: str = Field(nullable=False)
    longitude: str = Field(nullable=False)
    name: str = Field(nullable=False, index=True)
    created_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))
