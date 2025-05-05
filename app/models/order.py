from datetime import date


class Order:
    """
    Represents an order in the MarketFlow system.

    Attributes:
        id (int): Unique identifier of the order.
        client_id (int): ID of the client who made the order.
        product_id (int): ID of the product being ordered.
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
            id (int, optional): The unique identifier of the order.
            client_id (int): The client's ID.
            product_id (int): The product's ID.
            order_date (date, optional): Date of the order (defaults to today).
        """
        self.id = id
        self.client_id = client_id
        self.product_id = product_id
        self.order_date = order_date or date.today()

    def to_dict(self) -> dict:
        """
        Converts the order instance into a dictionary.

        Returns:
            dict: A dictionary with keys 'id', 'client_id', 'product_id', and 'order_date'.
        """
        return {
            "id": self.id,
            "client_id": self.client_id,
            "product_id": self.product_id,
            "order_date": self.order_date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates an Order instance from a dictionary.

        Args:
            data (dict): A dictionary containing order fields.

        Returns:
            Order: A populated Order object.
        """
        return cls(
            id=data.get("id"),
            client_id=data.get("client_id"),
            product_id=data.get("product_id"),
            order_date=data.get("order_date", date.today()),
        )

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the order.

        Returns:
            str: Representation showing all attributes.
        """
        return (
            f"<Order id={self.id} client_id={self.client_id} "
            f"product_id={self.product_id} order_date={self.order_date}>"
        )
