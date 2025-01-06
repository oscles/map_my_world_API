from app.domain.entities.category import Category
from app.domain.repositories.category_repository import CategoryRepository


class CreateCategoryUseCase:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def execute(self, category_data: Category) -> Category:
        return await self.category_repository.create(category_data)


class GetAllCategoriesUseCase:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def execute(self, offset: int = 0, limit: int = 100) -> Category:
        return await self.category_repository.all(offset, limit)
