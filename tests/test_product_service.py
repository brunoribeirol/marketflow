import pytest
from services.product_service import ProductService
from services.category_service import CategoryService
from repositories.product_repository import ProductRepository
from models.product import Product
from db.connection import get_db_connection, close_connection


@pytest.fixture(autouse=True)
def clear_products_table():
    """
    Clears the products and categories tables before each test.
    Ensures isolation and avoids data conflicts during test execution.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM categories")
    conn.commit()
    cursor.close()
    close_connection(conn)


def test_create_product_success():
    """
    Tests successful creation of a product with valid data.
    """
    category = CategoryService.create("Snacks")
    product = ProductService.create("Chips", 5.99, category.id)
    assert isinstance(product, Product)
    assert product.name == "Chips"
    assert product.price == 5.99
    assert product.category_id == category.id


def test_create_product_invalid_name():
    """
    Tests product creation with an empty name, expecting a validation error.
    """
    category = CategoryService.create("Drinks")
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        ProductService.create("", 10.0, category.id)


def test_create_product_invalid_price():
    """
    Tests product creation with zero or negative price, expecting a validation error.
    """
    category = CategoryService.create("Frozen")
    with pytest.raises(ValueError, match="Product price must be greater than zero."):
        ProductService.create("Pizza", 0, category.id)


def test_create_product_invalid_category():
    """
    Tests product creation with a non-existent category ID, expecting an error.
    """
    with pytest.raises(ValueError, match="Category not found."):
        ProductService.create("Juice", 3.5, 999)


def test_get_product_by_id_success():
    """
    Tests retrieving a product by its ID when it exists.
    """
    category = CategoryService.create("Cereal")
    created = ProductService.create("Corn Flakes", 6.5, category.id)
    fetched = ProductService.get_by_id(created.id)
    assert fetched.name == "Corn Flakes"


def test_get_product_by_id_not_found():
    """
    Tests retrieving a product by a non-existent ID.
    """
    with pytest.raises(ValueError, match="Product not found."):
        ProductService.get_by_id(999)


def test_list_all_products():
    """
    Tests listing all products after creating multiple entries.
    """
    category = CategoryService.create("Bakery")
    ProductService.create("Bread", 3.2, category.id)
    ProductService.create("Cake", 8.0, category.id)
    products = ProductService.list_all()
    assert len(products) == 2


def test_update_product_success():
    """
    Tests successful update of a product with valid data.
    """
    category = CategoryService.create("Dairy")
    created = ProductService.create("Milk", 4.0, category.id)
    updated = ProductService.update(created.id, "Skim Milk", 4.5, category.id)
    assert updated.name == "Skim Milk"
    assert updated.price == 4.5


def test_update_product_invalid_category():
    """
    Tests product update with an invalid category ID, expecting an error.
    """
    category = CategoryService.create("Pantry")
    product = ProductService.create("Sugar", 2.0, category.id)
    with pytest.raises(ValueError, match="Category not found."):
        ProductService.update(product.id, "Sugar", 2.0, 999)


def test_delete_product_success():
    """
    Tests successful deletion of an existing product.
    """
    category = CategoryService.create("Cleaning")
    product = ProductService.create("Soap", 1.99, category.id)
    result = ProductService.delete(product.id)
    assert result is True


def test_delete_product_not_found():
    """
    Tests deletion of a non-existent product ID, expecting an error.
    """
    with pytest.raises(ValueError, match="Product not found."):
        ProductService.delete(999)
