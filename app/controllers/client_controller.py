from services.client_service import ClientService
from app.utils.entity_display import list_entities


class ClientController:
    """
    Handles user interaction and orchestrates client-related actions.
    """

    @staticmethod
    def create():
        """
        Handles user input to create a new client and displays the result.
        """
        try:
            name = input("Enter client name: ")
            email = input("Enter client email: ")
            client = ClientService.create(name, email)
            print(
                f"\n✅ Client created successfully:\n- ID: {client.id}\n- Name: {client.name}\n- Email: {client.email}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")

    @staticmethod
    def list_all():
        """
        Retrieves and displays all registered clients.
        """
        clients = ClientService.list_all()
        if not clients:
            print("\n⚠️ No clients registered.\n")
            return

        print("\n📋 Registered Clients:")
        print()
        for client in clients:
            print(
                f"- ID: {client.id}\n- Name: {client.name}\n- Email: {client.email}\n"
            )

    @staticmethod
    def get_by_id():
        """
        Retrieves and displays a client by their ID.
        """
        try:
            list_entities(ClientService, "client")
            client_id = int(input("Enter client ID: "))
            client = ClientService.get_by_id(client_id)
            print(
                f"\n🔍 Client found:\n- ID: {client.id}\n- Name: {client.name}\n- Email: {client.email}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter a numeric ID.\n")

    @staticmethod
    def update():
        """
        Updates an existing client's data based on user input.
        """
        try:
            list_entities(ClientService, "client")
            client_id = int(input("Enter client ID to update: "))
            email = input("Enter new email: ")
            updated = ClientService.update(client_id, email)
            print(
                f"\n✅ Client updated successfully:\n- ID: {updated.id}\n- Name: {updated.name}\n- Email: {updated.email}\n"
            )
        except ValueError as ve:
            print(f"\n❌ {ve}\n")
        except Exception:
            print("\n❌ Invalid input. Please enter valid values.\n")
