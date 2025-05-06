from services.category_service import CategoryService


class CategoryController:
    """
    Handles user interaction and orchestrates category-related actions.
    """

    @staticmethod
    def create():
        """
        Handles user input to create a new category and displays the result.
        """
        try:
            name = input("Enter category name: ")
            category = CategoryService.create(name)
            print(f"\n✅ Category created successfully with ID {category.id}.\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")

    @staticmethod
    def list_all():
        """
        Retrieves and displays all registered categories.
        """
        categories = CategoryService.list_all()
        if not categories:
            print("\n⚠️ No categories registered.\n")
            return

        print("\n📦 Registered Categories:")
        for category in categories:
            print(f"- ID: {category.id}, Name: {category.name}")
        print()

    @staticmethod
    def get_by_id():
        """
        Retrieves and displays a category by its ID.
        """
        try:
            category_id = int(input("Enter category ID: "))
            category = CategoryService.get_by_id(category_id)
            print(
                f"\n🔍 Category found:\n- ID: {category.id}\n- Name: {category.name}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")

    @staticmethod
    def update():
        """
        Updates an existing category based on user input.
        """
        try:
            category_id = int(input("Enter category ID to update: "))
            name = input("Enter new category name: ")
            updated = CategoryService.update(category_id, name)
            print(f"\n✅ Category updated successfully: {updated}\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter valid values.\n")

    @staticmethod
    def delete():
        """
        Deletes a category based on ID with confirmation.
        """
        try:
            category_id = int(input("Enter category ID to delete: "))
            confirmed = input(
                f"Are you sure you want to delete category ID {category_id}? (y/n): "
            ).lower()
            if confirmed != "y":
                print("\n❎ Deletion canceled.\n")
                return

            CategoryService.delete(category_id)
            print("\n✅ Category deleted successfully.\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")
