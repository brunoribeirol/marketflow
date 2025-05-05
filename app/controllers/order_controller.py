from services.order_service import OrderService


class OrderController:
    """
    Handles user interaction and orchestrates order-related actions.
    """

    @staticmethod
    def create():
        try:
            client_id = int(input("Enter client ID: "))
            product_id = int(input("Enter product ID: "))
            order = OrderService.create(client_id, product_id)
            print(f"\n✅ Order created successfully with ID {order.id}.\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter valid values.\n")

    @staticmethod
    def list_all():
        orders = OrderService.list_all()
        if not orders:
            print("\n⚠️ No orders found.\n")
            return

        print("\n📦 Registered Orders:")
        for order in orders:
            print(
                f"- ID: {order.id}, Client ID: {order.client_id}, Product ID: {order.product_id}, Date: {order.order_date}"
            )
        print()

    @staticmethod
    def get_by_id():
        try:
            order_id = int(input("Enter order ID: "))
            order = OrderService.get_by_id(order_id)
            print(
                f"\n🔍 Order found:\n- ID: {order.id}\n- Client ID: {order.client_id}\n- Product ID: {order.product_id}\n- Date: {order.order_date}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")

    @staticmethod
    def delete():
        try:
            order_id = int(input("Enter order ID to delete: "))
            confirm = (
                input(f"Are you sure you want to delete order ID {order_id}? (y/n): ")
                .strip()
                .lower()
            )
            if confirm != "y":
                print("\n❎ Deletion cancelled.\n")
                return

            OrderService.delete(order_id)
            print("\n✅ Order deleted successfully.\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input.\n")
