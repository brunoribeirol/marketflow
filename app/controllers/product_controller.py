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
            print(f"\n✅ Product created successfully with ID {product.id}.\n")
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
        for p in products:
            print(
                f"- ID: {p.id}, Name: {p.name}, Price: ${p.price:.2f}, Category ID: {p.category_id}"
            )
        print()

    @staticmethod
    def get_by_id():
        """
        Retrieves and displays a product by its ID.
        """
        try:
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
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new name: ")
            price = float(input("Enter new price: "))
            category_id = int(input("Enter new category ID: "))

            updated = ProductService.update(product_id, name, price, category_id)
            print(f"\n✅ Product updated successfully: {updated}\n")
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
