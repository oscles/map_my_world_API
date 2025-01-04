from datetime import datetime
from typing import Optional

from sqlmodel import DateTime, Field, SQLModel


class Category(SQLModel, table=True):
    __tablename__ = "categories"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False, index=True)
    description: str = Field(nullable=False)
    created_at: Optional[DateTime] = Field(DateTime, default=datetime.now)
