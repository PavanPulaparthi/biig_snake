from http.client import PAYMENT_REQUIRED
from re import I


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} of {name} must be greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} of {name} must be greater than 0!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 1)
item1.apply_discount()

print(f"The total price of {item1.name} is {item1.calculate_total_price()}")

item2 = Item("Laptop", 1000, 1)
item2.pay_rate = 0.7
item2.apply_discount()
print(f"The total price of {item2.name} is {item2.calculate_total_price()}")

#item2.has_numpad = False

# print(Item.__dict__)    # All the attributes for Class level
# print(item1.__dict__)   # All the attributes for instance level