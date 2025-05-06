from db.connection import get_db_connection, close_connection
from models.client import Client
import queries.client_queries as q


class ClientRepository:
    """
    Handles all database operations related to the Client entity.
    """

    @staticmethod
    def create(name: str, email: str) -> int:
        """
        Inserts a new client into the database.

        Args:
            name (str): The name of the client.
            email (str): The email address of the client.

        Returns:
            int: The ID of the newly inserted client.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(q.CREATE_CLIENT, (name, email))
        conn.commit()
        client_id = cursor.lastrowid

        cursor.close()
        close_connection(conn)
        return client_id

    @staticmethod
    def get_by_id(client_id: int) -> Client | None:
        """
        Retrieves a client by ID.

        Args:
            client_id (int): The ID of the client to retrieve.

        Returns:
            Client | None: The Client object, or None if not found.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.GET_CLIENT_BY_ID, (client_id,))
        result = cursor.fetchone()

        cursor.close()
        close_connection(conn)

        return Client.from_dict(result) if result else None

    @staticmethod
    def list_all() -> list[Client]:
        """
        Retrieves all clients from the database.

        Returns:
            list[Client]: A list of all Client objects.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.GET_ALL_CLIENTS)
        results = cursor.fetchall()

        cursor.close()
        close_connection(conn)

        return [Client.from_dict(row) for row in results]

    @staticmethod
    def update(client_id: int, email: str) -> bool:
        """
        Updates a client's information by ID.

        Args:
            client_id (int): The ID of the client to update.
            email (str): The new email.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(q.UPDATE_CLIENT, (email, client_id))
        conn.commit()
        updated = cursor.rowcount > 0

        cursor.close()
        close_connection(conn)
        return updated

    @staticmethod
    def email_exists(email: str) -> bool:
        """
        Checks if a given email is already registered.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if the email exists, False otherwise.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.CHECK_EMAIL_EXISTS, (email,))
        result = cursor.fetchone()

        cursor.close()
        close_connection(conn)

        return result["count"] > 0
