CREATE_CLIENT = """
    INSERT INTO clients (name, email)
    VALUES (%s, %s)
"""

GET_CLIENT_BY_ID = """
    SELECT id, name, email
    FROM clients
    WHERE id = %s
"""

GET_ALL_CLIENTS = """
    SELECT id, name, email
    FROM clients
    ORDER BY id
"""

UPDATE_CLIENT = """
    UPDATE clients
    SET email = %s
    WHERE id = %s
"""

CHECK_EMAIL_EXISTS = """
    SELECT COUNT(*) as count
    FROM clients
    WHERE email = %s
"""
