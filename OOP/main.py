import csv

class Item:
    pay_rate = 0.8 # pay rate after 20% discount 
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to recieved arguments
        assert price >= 0, f"Price {price} is not >= zero."
        assert quantity >= 0, f"Quantity {quantity} is not >= zero."

        # Assign to self object
        self.name  = name
        self.price = price
        self.quantity = quantity 

        # Actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('/Users/joseservin/Automations/OOP/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Run validations to recieved arguments
        assert price >= 0, f"Price {price} is not >= zero."
        assert quantity >= 0, f"Quantity {quantity} is not >= zero."
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not >= zero."

        # Assign to self object
        self.name  = name
        self.price = price
        self.quantity = quantity 
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)

phone1 = Phone('ServinV10', 500, 5, 1)
phone2 = Phone('ServinV20', 700, 5, 1)

print(phone1.calculate_total_price())
print(phone2.calculate_total_price())