class Category:
    """
    Represents a category in the MarketFlow system.

    Attributes:
        id (int): Unique identifier of the category.
        name (str): Name of the category.
    """

    def __init__(self, id: int = None, name: str = ""):
        """
        Initializes a Category instance with basic sanitization.

        Args:
            id (int, optional): The category's unique identifier.
            name (str): The name of the category.
        """
        self.id = id
        self.name = name.strip()

    def to_dict(self) -> dict:
        """
        Converts the category instance into a dictionary.

        Returns:
            dict: A dictionary with keys 'id' and 'name'.
        """
        return {"id": self.id, "name": self.name}

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a Category instance from a dictionary.

        Args:
            data (dict): A dictionary containing category fields.

        Returns:
            Category: A populated Category object.
        """
        return cls(id=data.get("id"), name=data.get("name", ""))

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the category.

        Returns:
            str: Representation showing id and name.
        """
        return f"<Category id={self.id} name='{self.name}'>"
