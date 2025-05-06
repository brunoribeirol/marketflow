import pytest
from services.category_service import CategoryService
from repositories.category_repository import CategoryRepository
from models.category import Category
from db.connection import get_db_connection, close_connection


@pytest.fixture(autouse=True)
def clear_categories_table():
    """
    Clears the categories table before each test.
    Ensures that tests are isolated and do not interfere with each other.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categories")
    conn.commit()
    cursor.close()
    close_connection(conn)


def test_create_category_success():
    """
    Tests successful creation of a category with a valid name.
    """
    category = CategoryService.create("Beverages")
    assert isinstance(category, Category)
    assert category.name == "Beverages"


def test_create_category_empty_name():
    """
    Tests category creation with an empty name, expecting a validation error.
    """
    with pytest.raises(ValueError, match="Category name cannot be empty."):
        CategoryService.create("")


def test_create_category_duplicate_name():
    """
    Tests creation of a category with a name that already exists.
    Expects a duplicate name validation error.
    """
    CategoryService.create("Snacks")
    with pytest.raises(ValueError, match="Category name is already in use."):
        CategoryService.create("Snacks")


def test_get_category_by_id_success():
    """
    Tests retrieving a category by ID when it exists.
    """
    created = CategoryService.create("Bakery")
    fetched = CategoryService.get_by_id(created.id)
    assert fetched.name == "Bakery"


def test_get_category_by_id_not_found():
    """
    Tests retrieving a category by a non-existent ID.
    Expects a 'Category not found' error.
    """
    with pytest.raises(ValueError, match="Category not found."):
        CategoryService.get_by_id(999)


def test_list_all_categories():
    """
    Tests listing all categories after inserting two.
    """
    CategoryService.create("Fruits")
    CategoryService.create("Vegetables")
    categories = CategoryService.list_all()
    assert len(categories) == 2


def test_update_category_success():
    """
    Tests successful update of an existing category's name.
    """
    created = CategoryService.create("Old Category")
    updated = CategoryService.update(created.id, "New Category")
    assert updated.name == "New Category"


def test_update_category_to_existing_name():
    """
    Tests updating a category to a name that already exists.
    Expects a duplicate name validation error.
    """
    CategoryService.create("Cleaning")
    cat = CategoryService.create("Frozen")
    with pytest.raises(ValueError, match="Category name is already in use."):
        CategoryService.update(cat.id, "Cleaning")


def test_delete_category_success():
    """
    Tests successful deletion of an existing category.
    """
    category = CategoryService.create("To Delete")
    result = CategoryService.delete(category.id)
    assert result is True


def test_delete_category_not_found():
    """
    Tests deletion of a non-existent category ID.
    Expects a 'Category not found' error.
    """
    with pytest.raises(ValueError, match="Category not found."):
        CategoryService.delete(999)
