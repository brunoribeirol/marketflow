# queries/order_queries.py

CREATE_ORDER = """
    INSERT INTO orders (client_id, product_id, order_date)
    VALUES (%s, %s, %s)
"""

GET_ORDER_BY_ID = """
    SELECT o.id, o.client_id, o.product_id, o.order_date,
           c.name AS client_name, c.email AS client_email,
           p.name AS product_name, p.price AS product_price
    FROM orders o
    JOIN clients c ON o.client_id = c.id
    JOIN products p ON o.product_id = p.id
    WHERE o.id = %s
"""

GET_ALL_ORDERS = """
    SELECT o.id, o.client_id, o.product_id, o.order_date,
           c.name AS client_name, c.email AS client_email,
           p.name AS product_name, p.price AS product_price
    FROM orders o
    JOIN clients c ON o.client_id = c.id
    JOIN products p ON o.product_id = p.id
    ORDER BY o.id
"""

DELETE_ORDER = """
    DELETE FROM orders
    WHERE id = %s
"""

CHECK_ORDER_EXISTS = """
    SELECT COUNT(*) as count
    FROM orders
    WHERE id = %s
"""
