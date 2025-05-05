import time
from db.connection import get_db_connection, close_connection


def wait_for_db(retries=30, delay=2):
    """
    Waits until the database is ready by trying to connect.
    """
    for attempt in range(retries):
        try:
            conn = get_db_connection()
            close_connection(conn)
            print("✅ Database is ready!")
            return
        except Exception:
            print(f"⏳ Waiting for database... ({attempt + 1}/{retries})")
            time.sleep(delay)

    raise Exception("❌ Could not connect to the database after multiple attempts.")
