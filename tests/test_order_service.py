import pytest
from services.order_service import OrderService
from services.client_service import ClientService
from services.product_service import ProductService
from services.category_service import CategoryService
from models.order import Order
from db.connection import get_db_connection, close_connection


@pytest.fixture(autouse=True)
def clear_orders_table():
    """
    Clears the orders, products, categories, and clients tables before each test.
    Ensures test isolation and avoids data dependency between tests.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM categories")
    cursor.execute("DELETE FROM clients")
    conn.commit()
    cursor.close()
    close_connection(conn)


def create_valid_client_and_product():
    """
    Creates and returns a valid client and product for use in order tests.

    Returns:
        tuple: A tuple containing a valid client and product object.
    """
    client = ClientService.create("Order Test", "order@example.com")
    category = CategoryService.create("OrderCategory")
    product = ProductService.create("TestProduct", 10.0, category.id)
    return client, product


def test_create_order_success():
    """
    Tests successful creation of an order with valid client and product.
    """
    client, product = create_valid_client_and_product()
    order = OrderService.create(client.id, product.id)
    assert isinstance(order, Order)
    assert order.client_id == client.id
    assert order.product_id == product.id


def test_create_order_invalid_client():
    """
    Tests order creation failure when client does not exist.
    """
    _, product = create_valid_client_and_product()
    with pytest.raises(ValueError, match="Client not found."):
        OrderService.create(999, product.id)


def test_create_order_invalid_product():
    """
    Tests order creation failure when product does not exist.
    """
    client, _ = create_valid_client_and_product()
    with pytest.raises(ValueError, match="Product not found."):
        OrderService.create(client.id, 999)


def test_get_order_by_id_success():
    """
    Tests retrieving a specific order by ID when it exists.
    """
    client, product = create_valid_client_and_product()
    created = OrderService.create(client.id, product.id)
    fetched = OrderService.get_by_id(created.id)
    assert fetched.client_id == client.id
    assert fetched.product_id == product.id


def test_get_order_by_id_not_found():
    """
    Tests retrieving a non-existent order by ID.
    """
    with pytest.raises(ValueError, match="Order not found."):
        OrderService.get_by_id(999)


def test_list_all_orders():
    """
    Tests listing all orders after creating multiple records.
    """
    client, product = create_valid_client_and_product()
    OrderService.create(client.id, product.id)
    OrderService.create(client.id, product.id)
    orders = OrderService.list_all()
    assert len(orders) == 2


def test_delete_order_success():
    """
    Tests successful deletion of an existing order.
    """
    client, product = create_valid_client_and_product()
    order = OrderService.create(client.id, product.id)
    result = OrderService.delete(order.id)
    assert result is True


def test_delete_order_not_found():
    """
    Tests deleting a non-existent order and expects a failure.
    """
    with pytest.raises(ValueError, match="Order not found."):
        OrderService.delete(999)
