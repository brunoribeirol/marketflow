from app.utils.entity_display import list_entities
from services.order_service import OrderService
from services.client_service import ClientService
from services.product_service import ProductService


class OrderController:
    """
    Handles user interaction and orchestrates order-related actions.
    """

    @staticmethod
    def create():
        try:
            list_entities(ClientService, "client")
            list_entities(ProductService, "product")
            client_id = int(input("Enter client ID: "))
            product_id = int(input("Enter product ID: "))
            order = OrderService.create(client_id, product_id)
            client = ClientService.get_by_id(order.client_id)
            product = ProductService.get_by_id(order.product_id)

            print(
                f"\n✅ Order created successfully:\n"
                f"- ID: {order.id}\n"
                f"- Client: {client.name} ({client.email})\n"
                f"- Product: {product.name} - R${product.price:.2f}\n"
                f"- Date: {order.order_date}\n"
            )

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
        print()
        for order in orders:
            client = ClientService.get_by_id(order.client_id)
            product = ProductService.get_by_id(order.product_id)
            print(
                f"- ID: {order.id}\n"
                f"- Client: {client.name} ({client.email})\n"
                f"- Product: {product.name} - R${product.price:.2f}\n"
                f"- Date: {order.order_date}\n"
            )
        print()

    @staticmethod
    def get_by_id():
        try:
            list_entities(OrderService, "order")
            order_id = int(input("Enter order ID: "))
            order = OrderService.get_by_id(order_id)
            client = ClientService.get_by_id(order.client_id)
            product = ProductService.get_by_id(order.product_id)

            print(
                f"\n🔍 Order found:\n"
                f"- ID: {order.id}\n"
                f"- Client: {client.name} ({client.email})\n"
                f"- Product: {product.name} - R${product.price:.2f}\n"
                f"- Date: {order.order_date}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")
