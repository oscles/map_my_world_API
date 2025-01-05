from abc import ABC, abstractmethod
from typing import List

from ..entities.location import Location


class LocationRepository(ABC):
    @abstractmethod
    async def create(self, location: Location) -> Location:
        pass

    @abstractmethod
    async def all(self) -> List[Location] | None:
        pass
