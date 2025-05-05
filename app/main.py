from controllers.client_controller import ClientController


def show_menu():
    print("\n===== MarketFlow - Client Management =====")
    print("1. Create Client")
    print("2. List All Clients")
    print("3. Get Client by ID")
    print("4. Update Client")
    print("5. Delete Client")
    print("0. Exit")
    print("==========================================")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            ClientController.create_client()
        elif choice == "2":
            ClientController.list_all_clients()
        elif choice == "3":
            ClientController.get_client_by_id()
        elif choice == "4":
            ClientController.update_client()
        elif choice == "5":
            ClientController.delete_client()
        elif choice == "0":
            print("👋 Exiting... Goodbye!\n")
            break
        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
