from datetime import datetime, timedelta
from typing import List, Optional

from sqlmodel import Field, Session, SQLModel, or_, select

from app.domain.repositories.review_repository import LocationCategoryReviewRepository


class LocationCategoryReviewModel(SQLModel, table=True):
    __tablename__ = "location_category_reviewed"

    id: str = Field(primary_key=True, index=True, unique=True)
    location_id: str = Field(foreign_key="locations.id")
    category_id: str = Field(foreign_key="categories.id")
    last_reviewed_at: Optional[str] = Field(default=None)


class SQLLiteLocationCategoryReviewRepository(LocationCategoryReviewRepository):
    def __init__(self, session: Session):
        self.session = session

    async def get_recommendations(
        self,
        limit: int = 10,
    ) -> List[LocationCategoryReviewModel]:
        """
        Get 10 location-category combinations that need review, prioritizing those never reviewed
        and those not reviewed in the last 30 days.
        """

        # Subquery to get all reviewed combinations
        thirty_days_ago = datetime.now() - timedelta(days=30)

        needs_review = self.session.exec(
            select(LocationCategoryReviewModel)
            .where(
                or_(
                    LocationCategoryReviewModel.last_reviewed_at is None,
                    LocationCategoryReviewModel.last_reviewed_at < thirty_days_ago,
                )
            )
            .order_by(LocationCategoryReviewModel.last_reviewed_at)
            .limit(limit)
        ).all()

        return needs_review
