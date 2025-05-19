import time
import mysql.connector
from mysql.connector import Error
from config.config import DB_CONFIG


def get_db_connection(retries=30, delay=1):
    """
    Attempts to connect to the database, retrying if the connection fails.
    """
    for attempt in range(retries):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            if connection.is_connected():
                # print("✅ Successfully connected to the database.")
                return connection
        except Error as e:
            print(
                f"⏳ Attempt {attempt + 1}/{retries}: waiting for the database... (Error: {e})"
            )
            time.sleep(delay)

    raise ConnectionError(
        "❌ Failed to connect to the database after multiple attempts."
    )


def close_connection(connection):
    """
    Closes the database connection if it is open.
    """
    if connection and connection.is_connected():
        connection.close()
        # print("🔒 Database connection closed.")
