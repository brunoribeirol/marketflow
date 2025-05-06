import pytest
from db.connection import get_db_connection, close_connection
from services.client_service import ClientService
from models.client import Client


@pytest.fixture(autouse=True)
def clear_clients_table():
    """
    Clears the clients table before each test to ensure test isolation.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients")
    conn.commit()
    cursor.close()
    close_connection(conn)


def test_create_client_success():
    """
    Tests successful creation of a client with valid name and email.
    """
    client = ClientService.create("Test User", "test@example.com")
    assert isinstance(client, Client)
    assert client.name == "Test User"
    assert client.email == "test@example.com"


def test_create_client_empty_name():
    """
    Tests client creation with an empty name.
    Expects a validation error.
    """
    with pytest.raises(ValueError, match="Client name cannot be empty."):
        ClientService.create("", "test@example.com")


def test_create_client_invalid_email():
    """
    Tests client creation with an invalid email format.
    Expects a validation error.
    """
    with pytest.raises(ValueError, match="Invalid email format."):
        ClientService.create("Test", "invalid_email")


def test_get_client_by_id_success():
    """
    Tests fetching a client by ID when the client exists.
    """
    created = ClientService.create("Alice", "alice@example.com")
    fetched = ClientService.get_by_id(created.id)
    assert fetched.name == "Alice"
    assert fetched.email == "alice@example.com"


def test_get_client_by_id_not_found():
    """
    Tests fetching a client by a non-existent ID.
    Expects a 'Client not found' error.
    """
    with pytest.raises(ValueError, match="Client not found."):
        ClientService.get_by_id(999)


def test_list_all_clients():
    """
    Tests listing all clients after creating two clients.
    """
    ClientService.create("User A", "a@example.com")
    ClientService.create("User B", "b@example.com")
    clients = ClientService.list_all()
    assert len(clients) == 2


def test_update_client_success():
    """
    Tests updating an existing client's name and email.
    """
    created = ClientService.create("Old Name", "old@example.com")
    updated = ClientService.update(created.id, "New Name", "new@example.com")
    assert updated.name == "New Name"
    assert updated.email == "new@example.com"


def test_delete_client_success():
    """
    Tests successful deletion of a client.
    """
    client = ClientService.create("To Delete", "delete@example.com")
    result = ClientService.delete(client.id)
    assert result is True


def test_delete_client_not_found():
    """
    Tests deleting a non-existent client.
    Expects a 'Client not found' error.
    """
    with pytest.raises(ValueError, match="Client not found."):
        ClientService.delete(999)
