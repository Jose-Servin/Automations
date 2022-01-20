class User():
    def log(self):
        print(self)

class Teacher():
    def log(self):
        print('I am a teacher')

class Customer(User):
    def __init__(self, name, membership): # __init__ method represents the constructor
        self.name = name
        self.membership_type = membership
    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def reading_customer(): # static method: methods not attached to individual objects but instead are invoked on the Class
        print('Reading customer from DB')

    ############ Useful methods to override #################
    def __str__(self): # invoked anytime we want to convert a customer to a string; otherwise memory object gets returned 
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other): # without overiding equals method, python compares based off memory location
        if self.name == other.name:
            return True
        else:
            return False

    __hash__ = None

    __repr__ = __str__

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    @name.deleter
    def name(self):
        del self.name


customers = [
    Customer('Jose','Gold'),
    Customer('Baker','Pro'),
    Customer('Camila','Silver')
    ]

print(customers[0].membership_type)
customers[0].update_membership('Pro')
print(customers[0].membership_type)

Customer.reading_customer()
print(customers[0])

Customer.print_all_customers(customers)

print(customers[0] == customers[1])

print(customers)

customers[0].log()

users =  [
    Customer('Jose','Gold'),
    Customer('Baker','Pro'),
    Customer('Camila','Silver'),
    Teacher()
    ]

for user in users:
    user.log()