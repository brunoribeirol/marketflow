from controllers.client_controller import ClientController
from controllers.category_controller import CategoryController
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController


def main_menu():
    print("\n===== MarketFlow - Main Menu =====")
    print("1. Manage Clients")
    print("2. Manage Categories")
    print("3. Manage Products")
    print("4. Manage Orders")
    print("0. Exit")
    print("==================================")


def client_menu():
    print("\n===== Client Management =====")
    print("1. Create Client")
    print("2. List All Clients")
    print("3. Get Client by ID")
    print("4. Update Client")
    print("5. Delete Client")
    print("0. Back to Main Menu")
    print("=============================")


def category_menu():
    print("\n===== Category Management =====")
    print("1. Create Category")
    print("2. List All Categories")
    print("3. Get Category by ID")
    print("4. Update Category")
    print("5. Delete Category")
    print("0. Back to Main Menu")
    print("===============================")


def product_menu():
    print("\n===== Product Management =====")
    print("1. Create Product")
    print("2. List All Products")
    print("3. Get Product by ID")
    print("4. Update Product")
    print("5. Delete Product")
    print("0. Back to Main Menu")
    print("===============================")


def order_menu():
    print("\n===== Order Management =====")
    print("1. Create Order")
    print("2. List All Orders")
    print("3. Get Order by ID")
    print("4. Delete Order")
    print("0. Back to Main Menu")
    print("=============================")


def run_menu(controller, menu_function):
    while True:
        menu_function()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            controller.create()
        elif choice == "2":
            controller.list_all()
        elif choice == "3":
            controller.get_by_id()
        elif choice == "4":
            try:
                controller.update()
            except AttributeError:
                print("\n⚠️ This section does not support 'update' operations.\n")
        elif choice == "5":
            try:
                controller.delete()
            except AttributeError:
                print("\n⚠️ This section does not support 'delete' operations.\n")
        elif choice == "0":
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")


def main():
    while True:
        main_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_menu(ClientController, client_menu)
        elif choice == "2":
            run_menu(CategoryController, category_menu)
        elif choice == "3":
            run_menu(ProductController, product_menu)
        elif choice == "4":
            run_menu(OrderController, order_menu)
        elif choice == "0":
            print("\n👋 Exiting MarketFlow. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
