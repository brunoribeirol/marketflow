class Client:
    """
    Represents a client in the MarketFlow system.

    Attributes:
        id (int): Unique identifier of the client.
        name (str): Full name of the client.
        email (str): Email address of the client.
    """

    def __init__(self, id: int = None, name: str = "", email: str = ""):
        """
        Initializes a Client instance with basic sanitization.

        Args:
            id (int, optional): The client's unique identifier.
            name (str): The full name of the client.
            email (str): The client's email address.
        """
        self.id = id
        self.name = name.strip()
        self.email = email.strip().lower()

    def to_dict(self) -> dict:
        """
        Converts the client instance into a dictionary.

        Returns:
            dict: A dictionary with keys 'id', 'name', and 'email'.
        """
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a Client instance from a dictionary.

        Args:
            data (dict): A dictionary containing client fields.

        Returns:
            Client: A populated Client object.
        """
        return cls(
            id=data.get("id"), name=data.get("name", ""), email=data.get("email", "")
        )

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the client.

        Returns:
            str: Representation showing id, name, and email.
        """
        return f"<Client id={self.id} name='{self.name}' email='{self.email}'>"
