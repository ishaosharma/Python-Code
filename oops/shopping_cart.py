class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.index = self.items[1]
        if self.index != -1:
            self.items.pop(self.index)
    
    def get_total (self):
        self.total = 0
        for item in self.items:
            total += item.price
        return total
       

item1 = Item("Shirt", 20)
item2 = Item("Pants", 30)
item3 = Item("Shoes", 40)

cart = ShoppingCart()
cart.addItem(item1)
cart.addItem(item2)
cart.addItem(item3)

cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)
print(cart.get_total())

cart.remove_item(item2)
print(cart.get_total())


        

           



    
    