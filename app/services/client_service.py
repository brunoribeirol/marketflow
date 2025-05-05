from models.client import Client
from repositories.client_repository import ClientRepository


class ClientService:
    """
    Handles business logic for managing clients.
    """

    @staticmethod
    def create_client(name: str, email: str) -> Client:
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
        name = name.strip()
        email = email.strip().lower()

        if not name:
            raise ValueError("Client name cannot be empty.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        if ClientRepository.email_exists(email):
            raise ValueError("Email is already registered.")

        client_id = ClientRepository.create(name, email)
        return Client(id=client_id, name=name, email=email)

    @staticmethod
    def get_client_by_id(client_id: int) -> Client:
        """
        Retrieves a client by their ID.

        Args:
            client_id (int): The ID of the client to retrieve.

        Returns:
            Client: The corresponding Client object.

        Raises:
            ValueError: If the client is not found.
        """
        client = ClientRepository.get_by_id(client_id)
        if not client:
            raise ValueError("Client not found.")
        return client

    @staticmethod
    def get_all_clients() -> list[Client]:
        """
        Retrieves all registered clients.

        Returns:
            list[Client]: A list of all Client objects.
        """
        return ClientRepository.get_all()

    @staticmethod
    def update_client(client_id: int, name: str, email: str) -> Client:
        """
        Updates a client's information after validation.

        Args:
            client_id (int): The ID of the client to update.
            name (str): New name.
            email (str): New email.

        Returns:
            Client: The updated Client object.

        Raises:
            ValueError: If the client does not exist or inputs are invalid.
        """
        name = name.strip()
        email = email.strip().lower()

        if not name:
            raise ValueError("Client name cannot be empty.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")

        existing = ClientRepository.get_by_id(client_id)
        if not existing:
            raise ValueError("Client not found.")

        # Only check for duplication if email changed
        if existing.email != email and ClientRepository.email_exists(email):
            raise ValueError("Email is already registered.")

        updated = ClientRepository.update(client_id, name, email)
        if not updated:
            raise RuntimeError("Failed to update client.")

        return Client(id=client_id, name=name, email=email)

    @staticmethod
    def delete_client(client_id: int) -> bool:
        """
        Deletes a client by ID.

        Args:
            client_id (int): The ID of the client to delete.

        Returns:
            bool: True if deletion was successful.

        Raises:
            ValueError: If the client does not exist.
        """
        if not ClientRepository.get_by_id(client_id):
            raise ValueError("Client not found.")

        deleted = ClientRepository.delete(client_id)
        if not deleted:
            raise RuntimeError("Failed to delete client.")

        return True
