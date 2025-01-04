from datetime import datetime
from typing import Optional

from sqlmodel import DateTime, Field, SQLModel


class Location(SQLModel, table=True):
    __tablename__ = "locations"
    id: int | None = Field(default=None, primary_key=True)
    latitude: str = Field(nullable=False)
    longitude: str = Field(nullable=False)
    name: str = Field(nullable=False, index=True)
    created_at: Optional[DateTime] = Field(DateTime, default=datetime.now)
