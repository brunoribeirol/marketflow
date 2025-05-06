from models.category import Category
from repositories.category_repository import CategoryRepository


class CategoryService:
    """
    Handles business logic for managing categories.
    """

    @staticmethod
    def create(name: str) -> Category:
        """
        Creates a new category after validating input.

        Args:
            name (str): The name of the category.

        Returns:
            Category: The newly created Category object.

        Raises:
            ValueError: If the name is invalid or already in use.
        """
        name = name.strip()

        if not name:
            raise ValueError("Category name cannot be empty.")
        if CategoryRepository.name_exists(name):
            raise ValueError("Category name is already in use.")

        category_id = CategoryRepository.create(name)
        return Category(id=category_id, name=name)

    @staticmethod
    def get_by_id(category_id: int) -> Category:
        """
        Retrieves a category by ID.

        Args:
            category_id (int): The category's ID.

        Returns:
            Category: The corresponding Category object.

        Raises:
            ValueError: If the category is not found.
        """
        category = CategoryRepository.get_by_id(category_id)
        if not category:
            raise ValueError("Category not found.")
        return category

    @staticmethod
    def list_all() -> list[Category]:
        """
        Retrieves all categories.

        Returns:
            list[Category]: List of all Category objects.
        """
        return CategoryRepository.list_all()

    @staticmethod
    def update(category_id: int, name: str) -> Category:
        """
        Updates a category's name after validation.

        Args:
            category_id (int): ID of the category to update.
            name (str): New name.

        Returns:
            Category: The updated Category object.

        Raises:
            ValueError: If inputs are invalid or name already exists.
        """
        name = name.strip()
        if not name:
            raise ValueError("Category name cannot be empty.")

        existing = CategoryRepository.get_by_id(category_id)
        if not existing:
            raise ValueError("Category not found.")

        if existing.name != name and CategoryRepository.name_exists(name):
            raise ValueError("Category name is already in use.")

        updated = CategoryRepository.update(category_id, name)
        if not updated:
            raise RuntimeError("Failed to update category.")

        existing.name = name
        return existing

    @staticmethod
    def delete(category_id: int) -> bool:
        """
        Deletes a category by ID.

        Args:
            category_id (int): The ID of the category to delete.

        Returns:
            bool: True if deletion was successful.

        Raises:
            ValueError: If the category is not found.
        """
        if not CategoryRepository.get_by_id(category_id):
            raise ValueError("Category not found.")

        deleted = CategoryRepository.delete(category_id)
        if not deleted:
            raise RuntimeError("Failed to delete category.")

        return True
