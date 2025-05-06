CREATE_CATEGORY = """
    INSERT INTO categories (name)
    VALUES (%s)
"""

GET_CATEGORY_BY_ID = """
    SELECT id, name
    FROM categories
    WHERE id = %s
"""

GET_ALL_CATEGORIES = """
    SELECT id, name
    FROM categories
    ORDER BY id
"""

UPDATE_CATEGORY = """
    UPDATE categories
    SET name = %s
    WHERE id = %s
"""

DELETE_CATEGORY = """
    DELETE FROM categories
    WHERE id = %s
"""

CHECK_CATEGORY_NAME_EXISTS = """
    SELECT COUNT(*) as count
    FROM categories
    WHERE name = %s
"""
