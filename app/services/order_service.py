from datetime import date
from models.order import Order
from repositories.order_repository import OrderRepository
from repositories.client_repository import ClientRepository
from repositories.product_repository import ProductRepository
from utils.validators import validate_id


class OrderService:
    """
    Handles business logic for managing orders.
    """

    @staticmethod
    def create(client_id: int, product_id: int) -> Order:
        """
        Creates a new order after validating client and product existence.

        Args:
            client_id (int): The ID of the client.
            product_id (int): The ID of the product.

        Returns:
            Order: The newly created Order object.

        Raises:
            ValueError: If the client or product is not found.
        """
        client_id = validate_id(client_id, "Client ID")
        product_id = validate_id(product_id, "Product ID")

        if not ClientRepository.get_by_id(client_id):
            raise ValueError("Client not found.")
        if not ProductRepository.get_by_id(product_id):
            raise ValueError("Product not found.")

        order_id = OrderRepository.create(client_id, product_id)
        return Order(
            id=order_id,
            client_id=client_id,
            product_id=product_id,
            order_date=date.today(),
        )

    @staticmethod
    def get_by_id(order_id: int) -> Order:
        """
        Retrieves an order by ID.

        Args:
            order_id (int): The ID of the order.

        Returns:
            Order: The Order object.

        Raises:
            ValueError: If the order is not found.
        """
        order_id = validate_id(order_id, "Order ID")
        order = OrderRepository.get_by_id(order_id)
        if not order:
            raise ValueError("Order not found.")
        return order

    @staticmethod
    def list_all() -> list[Order]:
        """
        Retrieves all registered orders.

        Returns:
            list[Order]: A list of all Order objects.
        """
        return OrderRepository.list_all()
