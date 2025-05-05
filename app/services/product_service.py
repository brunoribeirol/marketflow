from models.product import Product
from repositories.product_repository import ProductRepository
from repositories.category_repository import CategoryRepository


class ProductService:
    """
    Handles business logic for managing products.
    """

    @staticmethod
    def create(name: str, price: float, category_id: int) -> Product:
        """
        Creates a new product after validating input data.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            category_id (int): The ID of the category the product belongs to.

        Returns:
            Product: The newly created Product object.

        Raises:
            ValueError: If the input data is invalid.
        """
        name = name.strip()

        if not name:
            raise ValueError("Product name cannot be empty.")
        if price <= 0:
            raise ValueError("Product price must be greater than zero.")
        if not CategoryRepository.get_by_id(category_id):
            raise ValueError("Category not found.")

        product_id = ProductRepository.create(name, price, category_id)
        return Product(id=product_id, name=name, price=price, category_id=category_id)

    @staticmethod
    def get_by_id(product_id: int) -> Product:
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The corresponding Product object.

        Raises:
            ValueError: If the product is not found.
        """
        product = ProductRepository.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found.")
        return product

    @staticmethod
    def list_all() -> list[Product]:
        """
        Retrieves all registered products.

        Returns:
            list[Product]: A list of all Product objects.
        """
        return ProductRepository.list_all()

    @staticmethod
    def update(product_id: int, name: str, price: float, category_id: int) -> Product:
        """
        Updates a product's information after validation.

        Args:
            product_id (int): The ID of the product to update.
            name (str): New name.
            price (float): New price.
            category_id (int): New category ID.

        Returns:
            Product: The updated Product object.

        Raises:
            ValueError: If the product does not exist or inputs are invalid.
        """
        name = name.strip()

        if not name:
            raise ValueError("Product name cannot be empty.")
        if price <= 0:
            raise ValueError("Product price must be greater than zero.")

        existing = ProductRepository.get_by_id(product_id)
        if not existing:
            raise ValueError("Product not found.")

        if not CategoryRepository.get_by_id(category_id):
            raise ValueError("Category not found.")

        updated = ProductRepository.update(product_id, name, price, category_id)
        if not updated:
            raise RuntimeError("Failed to update product.")

        return Product(id=product_id, name=name, price=price, category_id=category_id)

    @staticmethod
    def delete(product_id: int) -> bool:
        """
        Deletes a product by ID.

        Args:
            product_id (int): The ID of the product to delete.

        Returns:
            bool: True if deletion was successful.

        Raises:
            ValueError: If the product does not exist.
        """
        if not ProductRepository.get_by_id(product_id):
            raise ValueError("Product not found.")

        deleted = ProductRepository.delete(product_id)
        if not deleted:
            raise RuntimeError("Failed to delete product.")

        return True
