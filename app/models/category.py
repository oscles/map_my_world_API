import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Category(SQLModel, table=True):
    __tablename__ = "categories"
    id: uuid.UUID | None = Field(
        default_factory=uuid.uuid4, primary_key=True, nullable=False, index=True
    )
    name: str = Field(unique=True, nullable=False, index=True)
    description: str = Field(nullable=False)
    created_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))
