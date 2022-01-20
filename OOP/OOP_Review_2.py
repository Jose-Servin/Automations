class Customer():
    def __init__(self, name, membership):
        self.name = name
        self.membership_type = membership


customer_1 = Customer('jose','Gold')
print(customer_1.membership_type)