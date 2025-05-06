from models.product import Product
from repositories.product_repository import ProductRepository
from repositories.category_repository import CategoryRepository
from utils.validators import validate_name, validate_positive_price, validate_id


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
        name = validate_name(name, "Product name")
        price = validate_positive_price(price)
        category_id = validate_id(category_id, "Category ID")

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
        product_id = validate_id(product_id, "Product ID")
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
    def update(product_id: int, price: float) -> Product:
        """
        Updates a product's information after validation.

        Args:
            product_id (int): The ID of the product to update.
            price (float): New price.

        Returns:
            Product: The updated Product object.

        Raises:
            ValueError: If the product does not exist or inputs are invalid.
        """
        product_id = validate_id(product_id, "Product ID")
        price = validate_positive_price(price)

        existing = ProductRepository.get_by_id(product_id)
        if not existing:
            raise ValueError("Product not found.")

        if not ProductRepository.update(product_id, price):
            raise RuntimeError("Failed to update product.")

        existing.price = price
        return existing

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
        product_id = validate_id(product_id, "Product ID")
        if not ProductRepository.get_by_id(product_id):
            raise ValueError("Product not found.")
        return ProductRepository.delete(product_id)
