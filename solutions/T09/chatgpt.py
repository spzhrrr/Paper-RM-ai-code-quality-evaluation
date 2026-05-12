class InventoryManager:
    def __init__(self):
        self._inventory = {}

    def add_item(self, name, quantity, price):
        self._inventory[name] = {
            'name': name, 'quantity': quantity, 'price': price
        }

    def get_item(self, name):
        return self._inventory.get(name, None)

    def update_item(self, name, quantity=None, price=None):
        if name not in self._inventory:
            raise KeyError(f"Item '{name}' not found")
        if quantity is not None:
            self._inventory[name]['quantity'] = quantity
        if price is not None:
            self._inventory[name]['price'] = price

    def delete_item(self, name):
        if name not in self._inventory:
            raise KeyError(f"Item '{name}' not found")
        del self._inventory[name]

    def list_items(self):
        return list(self._inventory.values())
