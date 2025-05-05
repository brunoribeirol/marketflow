from utils.wait_for_db import wait_for_db
from db.connection import get_db_connection, close_connection


def test_connection():
    wait_for_db()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients")
        results = cursor.fetchall()

        print("✅ Connected successfully. Clients:")
        for row in results:
            print(row)

    except Exception as e:
        print(f"❌ Error connecting to DB: {e}")
    finally:
        cursor.close()
        close_connection(conn)


if __name__ == "__main__":
    test_connection()
