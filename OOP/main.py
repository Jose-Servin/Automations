class Item:
    pay_rate = 0.8 # pay rate after 20% discount 
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to recieved arguments
        assert price >= 0, f"Price {price} is not >= zero."
        assert quantity >= 0, f"Quantity {quantity} is not >= zero."

        # Assign to self object
        self.name  = name
        self.price = price
        self.quantity = quantity 
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)

print(Item.pay_rate) # accessing the Class /Global arrtribute 
print(item1.pay_rate) # accessing the Class /Global arrtribute 
print(item2.pay_rate) # accessing the Class /Global arrtribute 

print(Item.__dict__) # prints all attributes for Class level
print(item1.__dict__) # prints all attributes for instance level


print(item1.price)
item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
print(item2.price)
item2.apply_discount()
print(item2.price)