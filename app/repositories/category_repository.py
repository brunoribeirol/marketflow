from db.connection import get_db_connection, close_connection
from models.category import Category
import queries.category_queries as q


class CategoryRepository:
    """
    Handles all database operations related to the Category entity.
    """

    @staticmethod
    def create(name: str) -> int:
        """
        Inserts a new category into the database.

        Args:
            name (str): The name of the category.

        Returns:
            int: The ID of the newly inserted category.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(q.CREATE_CATEGORY, (name,))
        conn.commit()
        category_id = cursor.lastrowid

        cursor.close()
        close_connection(conn)
        return category_id

    @staticmethod
    def get_by_id(category_id: int) -> Category | None:
        """
        Retrieves a category by ID.

        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            Category | None: The Category object, or None if not found.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.GET_CATEGORY_BY_ID, (category_id,))
        result = cursor.fetchone()

        cursor.close()
        close_connection(conn)

        return Category.from_dict(result) if result else None

    @staticmethod
    def list_all() -> list[Category]:
        """
        Retrieves all categories from the database.

        Returns:
            list[Category]: A list of all Category objects.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.GET_ALL_CATEGORIES)
        results = cursor.fetchall()

        cursor.close()
        close_connection(conn)

        return [Category.from_dict(row) for row in results]

    @staticmethod
    def update(category_id: int, name: str) -> bool:
        """
        Updates a category's name by ID.

        Args:
            category_id (int): The ID of the category to update.
            name (str): The new name.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(q.UPDATE_CATEGORY, (name, category_id))
        conn.commit()
        updated = cursor.rowcount > 0

        cursor.close()
        close_connection(conn)
        return updated

    @staticmethod
    def delete(category_id: int) -> bool:
        """
        Deletes a category by ID.

        Args:
            category_id (int): The ID of the category to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(q.DELETE_CATEGORY, (category_id,))
        conn.commit()
        deleted = cursor.rowcount > 0

        cursor.close()
        close_connection(conn)
        return deleted

    @staticmethod
    def name_exists(name: str) -> bool:
        """
        Checks if a given category name is already registered.

        Args:
            name (str): The category name to check.

        Returns:
            bool: True if the name exists, False otherwise.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.CHECK_CATEGORY_NAME_EXISTS, (name,))
        result = cursor.fetchone()

        cursor.close()
        close_connection(conn)

        return result["count"] > 0
