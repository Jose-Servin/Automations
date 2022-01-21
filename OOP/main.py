# Only used to instantiate instances 

from item import Item
#from phone import Phone

item1 = Item('MyItem', 750)
#item1.name = 'Other Name' # will return an AttributeError because of the name property defined

print(item1.name)