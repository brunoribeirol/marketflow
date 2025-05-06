from app.utils.entity_display import list_entities
from services.product_service import ProductService


class ProductController:
    """
    Handles user interaction and orchestrates product-related actions.
    """

    @staticmethod
    def create():
        """
        Handles user input to create a new product and displays the result.
        """
        try:
            from services.category_service import CategoryService

            categories = CategoryService.list_all()
            if not categories:
                print("\n⚠️ No categories available. Please add a category first.\n")
                return

            print("\n📦 Available Categories:")
            for cat in categories:
                print(f"- ID: {cat.id}, Name: {cat.name}")
            print()

            name = input("Enter product name: ").strip()
            price = float(input("Enter product price: $"))
            category_id = int(input("Enter category ID: "))

            product = ProductService.create(name, price, category_id)
            print(
                f"\n✅ Product created successfully:\n- ID: {product.id}\n- Name: {product.name}\n- Price: {product.price}\n- Category ID: {product.category_id}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}\n")

    @staticmethod
    def list_all():
        """
        Retrieves and displays all registered products.
        """
        products = ProductService.list_all()
        if not products:
            print("\n⚠️ No products registered.\n")
            return

        print("\n📦 Registered Products:")
        print()
        for product in products:
            print(
                f"- ID: {product.id}\n- Name: {product.name}\n- Price: ${product.price:.2f}\n- Category ID: {product.category_id}\n"
            )

    @staticmethod
    def get_by_id():
        """
        Retrieves and displays a product by its ID.
        """
        try:
            list_entities(ProductService, "product")
            product_id = int(input("Enter product ID: "))
            product = ProductService.get_by_id(product_id)
            print(
                f"\n🔍 Product found:\n- ID: {product.id}\n- Name: {product.name}\n- Price: ${product.price:.2f}\n- Category ID: {product.category_id}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")

    @staticmethod
    def update():
        """
        Updates an existing product's data based on user input.
        """
        try:
            list_entities(ProductService, "product")
            product_id = int(input("Enter product ID to update: "))
            price = float(input("Enter new price: "))

            updated = ProductService.update(product_id, price)
            print(
                f"\n✅ Product updated successfully:\n- ID: {updated.id}\n- Name: {updated.name}\n- Price: ${updated.price:.2f}\n- Category ID: {updated.category_id}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}\n")

    @staticmethod
    def delete():
        """
        Deletes a product based on its ID, with confirmation.
        """
        try:
            list_entities(ProductService, "product")
            product_id = int(input("Enter product ID to delete: "))
            confirmed = input(
                f"Are you sure you want to delete product ID {product_id}? (y/n): "
            ).lower()
            if confirmed != "y":
                print("\n❎ Deletion canceled.\n")
                return

            ProductService.delete(product_id)
            print("\n✅ Product deleted successfully.\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")
