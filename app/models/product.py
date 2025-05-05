class Product:
    """
    Represents a product in the MarketFlow system.

    Attributes:
        id (int): Unique identifier of the product.
        name (str): Name of the product.
        price (float): Price of the product.
        category_id (int): ID of the category the product belongs to.
    """

    def __init__(
        self,
        id: int = None,
        name: str = "",
        price: float = 0.0,
        category_id: int = None,
    ):
        """
        Initializes a Product instance with basic sanitization.

        Args:
            id (int, optional): The product's unique identifier.
            name (str): The name of the product.
            price (float): The product's price.
            category_id (int): ID of the related category.
        """
        self.id = id
        self.name = name.strip()
        self.price = round(float(price), 2)
        self.category_id = category_id

    def to_dict(self) -> dict:
        """
        Converts the product instance into a dictionary.

        Returns:
            dict: A dictionary with product fields.
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
            data (dict): A dictionary with product fields.

        Returns:
            Product: A populated Product object.
        """
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            price=data.get("price", 0.0),
            category_id=data.get("category_id"),
        )

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the product.

        Returns:
            str: Representation showing id, name, price, and category_id.
        """
        return (
            f"<Product id={self.id} name='{self.name}' "
            f"price={self.price} category_id={self.category_id}>"
        )
