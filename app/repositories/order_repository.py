from datetime import date
from db.connection import get_db_connection, close_connection
from models.order import Order
import queries.order_queries as q


class OrderRepository:
    """
    Handles all database operations related to the Order entity.
    """

    @staticmethod
    def create(client_id: int, product_id: int) -> int:
        """
        Inserts a new order into the database.

        Args:
            client_id (int): The ID of the client placing the order.
            product_id (int): The ID of the product being ordered.

        Returns:
            int: The ID of the newly created order.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        order_date = date.today()
        cursor.execute(q.CREATE_ORDER, (client_id, product_id, order_date))
        conn.commit()
        order_id = cursor.lastrowid

        cursor.close()
        close_connection(conn)
        return order_id

    @staticmethod
    def get_by_id(order_id: int) -> Order | None:
        """
        Retrieves an order by its ID.

        Args:
            order_id (int): The ID of the order.

        Returns:
            Order | None: The Order object, or None if not found.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.GET_ORDER_BY_ID, (order_id,))
        result = cursor.fetchone()

        cursor.close()
        close_connection(conn)
        return Order.from_dict(result) if result else None

    @staticmethod
    def list_all() -> list[Order]:
        """
        Retrieves all orders from the database.

        Returns:
            list[Order]: A list of all Order objects.
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(q.GET_ALL_ORDERS)
        results = cursor.fetchall()

        cursor.close()
        close_connection(conn)

        return [Order.from_dict(row) for row in results]
