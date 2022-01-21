for instance in Item.all:
    print(instance.name)
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


item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)