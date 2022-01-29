from main import Scooter
from main import ElectricCar
from main import Car
from main import Bike
from main import Skateboard
from main import Calculator

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

tesla = ElectricCar('Red',2021, 'Tesla','Model Y',120)
tesla.details()
ElectricCar.wheels = 4
print(ElectricCar.wheel_info())
print(tesla.insurance.company)

tesla.insurance.company = 'DallasInsurance'
print(tesla.insurance.company)


# Creating a Bike instance

mongoose = Bike(22)
mongoose.check_wheels()

print(mongoose.alloy_wheels)

# Using super method to call parent class function in child class
tesla.parent_class_year()



######## DO THIS TO CALL A METHOD FROM ANOTHER CLASS (DUCK TYPING)
# Create instance of Bike
bike_instance = Bike(12)
# create instance of Scooter
scooter_1 = Scooter()
# use method in scooter that takes in Bike instance as an argument 
scooter_1.use_method_from_other_class(bike_instance)

# Create instance of Skateboard 
skateboard_1 = Skateboard()
# create instance of Scooter
scooter_2 = Scooter()
# use method in Scooter that takes in Object_from_class as an argument
scooter_2.use_method_from_other_class(skateboard_1)



### MAGIC METHOD (Learn more about this topic) ###################################################
my_tesla = ElectricCar('Blue',2021,'Tesla','Model X', 520)
your_tesla = ElectricCar('Red',2021, 'Tesla','Model Y', 480)

total_kW = my_tesla + your_tesla
print(total_kW)

### __str__ Magic Method Overloading
print(my_tesla)
print(my_car)


####### METHOD OVERLOADING ############
cal_1 = Calculator()

print(cal_1.take_sum(4))

print(cal_1.take_sum_args(10,10,10,10,5,5,4))