from datetime import datetime
from typing import Annotated, Optional
from uuid import uuid4

from fastapi import Query
from sqlmodel import Field, Session, SQLModel, select

from app.domain.entities.category import Category
from app.domain.repositories.category_repository import CategoryRepository


class CategoryModel(SQLModel, table=True):
    __tablename__ = "categories"

    id: str | None = Field(
        default_factory=lambda: str(uuid4()), primary_key=True, index=True, unique=True
    )
    name: str = Field(unique=True, nullable=False, index=True)
    description: str = Field(nullable=False)
    created_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))


class SQLLiteCategoryRepository(CategoryRepository):
    def __init__(self, session: Session):
        self.session = session

    async def create(self, category: Category) -> Category:
        db_category = CategoryModel(
            name=category.name, description=category.description
        )

        self.session.add(db_category)
        self.session.commit()
        self.session.refresh(db_category)

        return Category(
            id=db_category.id,
            name=db_category.name,
            description=db_category.description,
            created_at=db_category.created_at,
        )

    async def all(
        self,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
    ):
        categories = self.session.exec(
            select(CategoryModel).offset(offset).limit(limit)
        ).all()

        return categories
