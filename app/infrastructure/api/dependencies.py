from app.infrastructure.database import get_session
from app.infrastructure.repositories.sqllite_location_repository import (
    SQLLiteLocationRepository,
)


def get_location_repository():
    return SQLLiteLocationRepository(next(get_session()))
