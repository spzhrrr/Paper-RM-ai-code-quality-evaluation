class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity, price):
        self.inventory[name] = {
            'name': name,
            'quantity': quantity,
            'price': price
        }

    def get_item(self, name):
        if name in self.inventory:
            return self.inventory[name]
        return None

    def update_item(self, name, quantity=None, price=None):
        if name not in self.inventory:
            raise KeyError(f'{name} not found in inventory')
        if quantity is not None:
            self.inventory[name]['quantity'] = quantity
        if price is not None:
            self.inventory[name]['price'] = price

    def delete_item(self, name):
        if name not in self.inventory:
            raise KeyError(f'{name} not found in inventory')
        del self.inventory[name]

    def list_items(self):
        return list(self.inventory.values())
