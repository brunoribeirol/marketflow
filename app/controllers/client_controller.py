from services.client_service import ClientService
from models.client import Client


class ClientController:
    """
    Handles user interaction and orchestrates client-related actions.
    """

    @staticmethod
    def create_client():
        """
        Handles user input to create a new client and displays the result.
        """
        try:
            name = input("Enter client name: ")
            email = input("Enter client email: ")
            client = ClientService.create_client(name, email)
            print(f"\n✅ Client created successfully with ID {client.id}.\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")

    @staticmethod
    def list_all_clients():
        """
        Retrieves and displays all registered clients.
        """
        clients = ClientService.get_all_clients()
        if not clients:
            print("\n⚠️ No clients registered.\n")
            return

        print("\n📋 Registered Clients:")
        for client in clients:
            print(f"- ID: {client.id}, Name: {client.name}, Email: {client.email}")
        print()

    @staticmethod
    def get_client_by_id():
        """
        Retrieves and displays a client by their ID.
        """
        try:
            client_id = int(input("Enter client ID: "))
            client = ClientService.get_client_by_id(client_id)
            print(
                f"\n🔍 Client found:\n- ID: {client.id}\n- Name: {client.name}\n- Email: {client.email}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")

    @staticmethod
    def update_client():
        """
        Updates an existing client's data based on user input.
        """
        try:
            client_id = int(input("Enter client ID to update: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            updated = ClientService.update_client(client_id, name, email)
            print(f"\n✅ Client updated successfully: {updated}\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter valid values.\n")

    @staticmethod
    def delete_client():
        """
        Deletes a client based on their ID, with confirmation.
        """
        try:
            client_id = int(input("Enter client ID to delete: "))
            confirmed = input(
                f"Are you sure you want to delete client ID {client_id}? (y/n): "
            ).lower()
            if confirmed != "y":
                print("\n❎ Deletion canceled.\n")
                return

            ClientService.delete_client(client_id)
            print(f"\n✅ Client deleted successfully.\n")
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")
