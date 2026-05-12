class InventoryManager:
    """Manage a product inventory with full CRUD operations.

    Storage is backed by a dict keyed on item name.
    All single-item operations run in O(1) average time.
    """

    def __init__(self):
        self._items: dict = {}

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add a new item or overwrite an existing entry.

        Args:
            name: Unique item identifier.
            quantity: Stock quantity (non-negative integer).
            price: Unit price (non-negative float).
        """
        self._items[name] = {'name': name, 'quantity': quantity, 'price': price}

    def get_item(self, name: str) -> dict | None:
        """Return the item dict for name, or None if not present."""
        return self._items.get(name)

    def update_item(self, name: str, quantity: int = None,
                    price: float = None) -> None:
        """Update quantity and/or price of an existing item.

        Raises:
            KeyError: If name is not present in the inventory.
        """
        if name not in self._items:
            raise KeyError(f"Item '{name}' does not exist in inventory")
        if quantity is not None:
            self._items[name]['quantity'] = quantity
        if price is not None:
            self._items[name]['price'] = price

    def delete_item(self, name: str) -> None:
        """Remove an item from the inventory.

        Raises:
            KeyError: If name is not present in the inventory.
        """
        if name not in self._items:
            raise KeyError(f"Item '{name}' does not exist in inventory")
        del self._items[name]

    def list_items(self) -> list:
        """Return a list of all item dicts."""
        return list(self._items.values())
