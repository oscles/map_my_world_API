from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class Category(BaseModel):
    id: UUID | None
    name: str = Field(..., description="Name of the category")
    description: str = Field(..., description="Description of the category")
    created_at: datetime = Field(
        default_factory=datetime.now, description="Creation timestamp"
    )
