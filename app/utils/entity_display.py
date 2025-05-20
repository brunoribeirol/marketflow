import inflect
from services.category_service import CategoryService

def list_entities(service, entity_name):
    """
    Dynamically prints all fields of each entity returned by the service's list_all method.

    Args:
        service: The service class that provides the list_all() method.
        entity_name (str): The name of the entity type (for display only).
    """
    p = inflect.engine()
    try:
        items = service.list_all()
        if not items:
            print(f"\nℹ️ No registered {p.plural(entity_name)} found.")
            return

        plural_name = p.plural(entity_name)
        print(f"\n📦 Registered {plural_name.capitalize()}:")

        for item in items:
            attributes = vars(item)

            # Se for produto, carrega dicionário {id: name} das categorias
            category_names = {}
            if entity_name == "product":
                category_names = {c.id: c.name for c in CategoryService.list_all()}

            print("\n" + "\n".join([
                f"- {key.capitalize()}: {category_names[value] if entity_name == 'product' and key == 'category_id' else format_value(key, value)}"
                for key, value in attributes.items()
            ]))

        print()
    except Exception as e:
        print(f"❌ Failed to load {entity_name}s: {e}")


def format_value(key, value):
    """
    Applies custom formatting for specific fields if needed.
    Example: formats 'price' as currency.
    """
    if "price" in key.lower() and isinstance(value, (int, float)):
        return f"${value:.2f}"
    return value
