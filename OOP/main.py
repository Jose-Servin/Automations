# Only used to instantiate instances 

from item import Item
#from phone import Phone

item1 = Item('MyItem', 750)
#item1.name = 'Other Name' # will return an AttributeError because of the name property defined
item1.name = 'Other Name' # after using a setter, no errors returned
print(item1.name)

print(item1.price)
item1.apply_increment(0.2)
print(item1.price)
item1.apply_discount()
print(item1.price)