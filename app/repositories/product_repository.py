from db.connection import get_db_connection, close_connection
from models.product import Product
import queries.product_queries as q


class ProductRepository:
    """
    Handles all database operations related to the Product entity.
    """

    @staticmethod
    def create(name: str, price: float, category_id: int) -> int:
        """
        Inserts a new product into the database.

        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            category_id (int): ID of the associated category.

        Returns:
            int: ID of the newly inserted product.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(q.CREATE_PRODUCT, (name, price, category_id))
        conn.commit()
        product_id = cursor.lastrowid

        cursor.close()
        close_connection(conn)
        return product_id

    @staticmethod
    def get_by_id(product_id: int) -> Product | None:
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): Product ID.

        Returns:
            Product | None: Product instance or None if not found.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.GET_PRODUCT_BY_ID, (product_id,))
        result = cursor.fetchone()

        cursor.close()
        close_connection(conn)
        return Product.from_dict(result) if result else None

    @staticmethod
    def list_all() -> list[Product]:
        """
        Retrieves all products from the database.

        Returns:
            list[Product]: A list of all product records.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.GET_ALL_PRODUCTS)
        results = cursor.fetchall()

        cursor.close()
        close_connection(conn)
        return [Product.from_dict(row) for row in results]

    @staticmethod
    def update(product_id: int, name: str, price: float, category_id: int) -> bool:
        """
        Updates a product's data.

        Args:
            product_id (int): ID of the product to update.
            name (str): New name.
            price (float): New price.
            category_id (int): New category ID.

        Returns:
            bool: True if update was successful, False otherwise.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(q.UPDATE_PRODUCT, (name, price, category_id, product_id))
        conn.commit()
        updated = cursor.rowcount > 0

        cursor.close()
        close_connection(conn)
        return updated

    @staticmethod
    def delete(product_id: int) -> bool:
        """
        Deletes a product by ID.

        Args:
            product_id (int): Product ID to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(q.DELETE_PRODUCT, (product_id,))
        conn.commit()
        deleted = cursor.rowcount > 0

        cursor.close()
        close_connection(conn)
        return deleted

    @staticmethod
    def name_exists(name: str) -> bool:
        """
        Checks if a product name already exists in the database.

        Args:
            name (str): Name to check.

        Returns:
            bool: True if name exists, False otherwise.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.CHECK_PRODUCT_NAME_EXISTS, (name,))
        result = cursor.fetchone()

        cursor.close()
        close_connection(conn)
        return result["count"] > 0
