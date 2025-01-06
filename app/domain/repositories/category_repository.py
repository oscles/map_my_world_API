from abc import ABC, abstractmethod
from typing import List

from ..entities.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    async def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    async def all(self, offset: int = 0, limit: int = 100) -> List[Category] | None:
        pass
