CREATE_PRODUCT = """
    INSERT INTO products (name, price, category_id)
    VALUES (%s, %s, %s)
"""

GET_PRODUCT_BY_ID = """
    SELECT id, name, price, category_id
    FROM products
    WHERE id = %s
"""

GET_ALL_PRODUCTS = """
    SELECT id, name, price, category_id
    FROM products
    ORDER BY id
"""

UPDATE_PRODUCT = """
    UPDATE products
    SET name = %s, price = %s, category_id = %s
    WHERE id = %s
"""

DELETE_PRODUCT = """
    DELETE FROM products
    WHERE id = %s
"""

CHECK_PRODUCT_NAME_EXISTS = """
    SELECT COUNT(*) as count
    FROM products
    WHERE name = %s
"""
