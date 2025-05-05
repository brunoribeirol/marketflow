from datetime import date


class Order:
    """
    Represents a product order made by a client in the MarketFlow system.

    Attributes:
        id (int): Unique identifier of the order.
        client_id (int): ID of the client who placed the order.
        product_id (int): ID of the product that was ordered.
        order_date (date): Date when the order was placed.
    """

    def __init__(
        self,
        id: int = None,
        client_id: int = None,
        product_id: int = None,
        order_date: date = None,
    ):
        """
        Initializes an Order instance.

        Args:
            id (int, optional): The order ID.
            client_id (int): The ID of the client who made the order.
            product_id (int): The ID of the product being ordered.
            order_date (date, optional): The date of the order. Defaults to today.
        """
        self.id = id
        self.client_id = client_id
        self.product_id = product_id
        self.order_date = order_date or date.today()

    def to_dict(self) -> dict:
        """
        Converts the order instance into a dictionary.

        Returns:
            dict: A dictionary with keys 'id', 'client_id', 'product_id', 'order_date'.
        """
        return {
            "id": self.id,
            "client_id": self.client_id,
            "product_id": self.product_id,
            "order_date": str(self.order_date),
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates an Order instance from a dictionary.

        Args:
            data (dict): Dictionary containing order fields.

        Returns:
            Order: A populated Order object.
        """
        return cls(
            id=data.get("id"),
            client_id=data.get("client_id"),
            product_id=data.get("product_id"),
            order_date=(
                date.fromisoformat(data.get("order_date"))
                if data.get("order_date")
                else None
            ),
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the order.

        Returns:
            str: Representation showing id, client, product and date.
        """
        return (
            f"<Order id={self.id} client_id={self.client_id} "
            f"product_id={self.product_id} order_date={self.order_date}>"
        )
