from models.client import Client
from repositories.client_repository import ClientRepository
from utils.validators import validate_name, validate_email, validate_id


class ClientService:
    """
    Handles business logic for managing clients.
    """

    @staticmethod
    def create(name: str, email: str) -> Client:
        """
        Creates a new client after validating input data.

        Args:
            name (str): The client's full name.
            email (str): The client's email address.

        Returns:
            Client: The newly created Client object.

        Raises:
            ValueError: If the input data is invalid or email is already in use.
        """
        name = validate_name(name, "Client name")
        email = validate_email(email)

        if ClientRepository.email_exists(email):
            raise ValueError("Email is already registered.")

        client_id = ClientRepository.create(name, email)
        return Client(id=client_id, name=name, email=email)

    @staticmethod
    def get_by_id(client_id: int) -> Client:
        """
        Retrieves a client by their ID.

        Args:
            client_id (int): The ID of the client to retrieve.

        Returns:
            Client: The corresponding Client object.

        Raises:
            ValueError: If the client is not found.
        """
        client_id = validate_id(client_id, "Client ID")
        client = ClientRepository.get_by_id(client_id)
        if not client:
            raise ValueError("Client not found.")
        return client

    @staticmethod
    def list_all() -> list[Client]:
        """
        Retrieves all registered clients.

        Returns:
            list[Client]: A list of all Client objects.
        """
        return ClientRepository.list_all()

    @staticmethod
    def update(client_id: int, email: str) -> Client:
        """
        Updates a client's information after validation.

        Args:
            client_id (int): The ID of the client to update.
            email (str): New email.

        Returns:
            Client: The updated Client object.

        Raises:
            ValueError: If the client does not exist or inputs are invalid.
        """
        client_id = validate_id(client_id, "Client ID")
        email = validate_email(email)

        existing = ClientRepository.get_by_id(client_id)
        if not existing:
            raise ValueError("Client not found.")

        if existing.email != email and ClientRepository.email_exists(email):
            raise ValueError("Email is already registered.")

        if not ClientRepository.update(client_id, email):
            raise RuntimeError("Failed to update client.")

        existing.email = email
        return existing
