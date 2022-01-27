from main import Car

my_car = Car('sonic grey', 2021, 'Honda', 'Accord')
my_car.details()

my_car2 = Car('grey',2015,'Chevy','Malibu')

# Testing to see how Static variables/Class variables are also a part of individual instances
print(my_car.wheels)
print(my_car2.wheels)

Car.wheels = 5 # to modify Class Variables you use the Class namespace
print(my_car.wheels)
print(my_car2.wheels)

Car.wheels = 6

# Testing the Class Method created 
print(Car.wheel_info())

# Testing the static method 
Car.info()

# Testing show_info method
my_car.show_info()

# Accessing the inner class Insurance variables
print(my_car.insurance.company)

# Creating instance (object) for inner class
car1_insurance = my_car.insurance
print(car1_insurance.rate)

# Creating instance of inner class outside the outer class
default_insurance = Car.Insurance()
print(default_insurance.company)

# Creating instance of inner class outside the outer class with non-default arguments
high_insurance = Car.Insurance('Geiko', 200)
print(high_insurance.rate)

# Creating instance of inner class via Outter class with non-default arguments
my_car3 = Car('Red',2010, 'Chevy','Trailblazer')
car3_insurance = my_car3.insurance
car3_insurance.company = 'TAMU Insurance'
car3_insurance.rate = 1212

print(car3_insurance.rate, car3_insurance.company)

my_car3.show_info()