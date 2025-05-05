class Product:
    """
    Represents a product available for purchase in the MarketFlow system.

    Attributes:
        id (int): Unique identifier of the product.
        name (str): Product name (e.g., 'Apple', 'Salmon Fillet').
        price (float): Price of the product in the local currency.
        category_id (int): Foreign key referencing the product's category.
    """

    def __init__(
        self,
        id: int = None,
        name: str = "",
        price: float = 0.0,
        category_id: int = None,
    ):
        """
        Initializes a Product instance.

        Args:
            id (int, optional): Product ID (usually from the database).
            name (str): Name of the product.
            price (float): Product price. Must be non-negative.
            category_id (int): ID of the associated category.

        Raises:
            ValueError: If price is negative.
        """
        self.id = id
        self.name = name.strip()

        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = round(price, 2)

        self.category_id = category_id

    def to_dict(self) -> dict:
        """
        Converts the product instance into a dictionary.

        Returns:
            dict: A dictionary with keys 'id', 'name', 'price', 'category_id'.
        """
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category_id": self.category_id,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a Product instance from a dictionary.

        Args:
            data (dict): Dictionary containing product fields.

        Returns:
            Product: A populated Product object.
        """
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            price=float(data.get("price", 0.0)),
            category_id=data.get("category_id"),
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
            str: Representation showing id, name, price and category_id.
        """
        return f"<Product id={self.id} name='{self.name}' price={self.price} category_id={self.category_id}>"
