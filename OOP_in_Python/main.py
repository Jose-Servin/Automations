
class Car:

    # Class variables are called Static Variables 
    wheels = 4

    # idea behind __init__ is that this method will get called once automatically per object 
    def __init__(self, color, year, make, model ): # grey 2021 Honda Accord 
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.insurance = self.Insurance() #creating instance of inner class in outer class 

    def details(self):
        print(f'Your vehicle info is {self.color}, {self.year}, {self.make}, {self.model}.')


    # Accessor Methods: fetch value of instance variable 
    def get_year(self):
        return self.year

    # Mutator Methods: set new values to instance variable 
    def set_color(self, new_color):
        self.color = new_color

    @classmethod
    def wheel_info(cls):
        return cls.wheels
    
    # static methods do not take concern over Class or Instances 
    @staticmethod
    def info():
        print('This method has nothing to do with Class or Instances')


    def show_info(self):
        print(f'This car is a {self.year}, {self.make} {self.model}. ')
        self.insurance.show_info() # in the outter class, call the inner class function 
    
    def __str__(self):
        return (f'You have a {self.make} {self.model}')

    
    class Insurance:
        def __init__(self, company='StateFarm', rate=165):
            self.company = company
            self.rate = rate

        def show_info(self):
            print(f'Your insurance company is {self.company} and you pay ${self.rate} per month.')

class ElectricCar(Car):

    def __init__(self, color, year, make, model, kilowatts):
        super().__init__(color, year, make, model) # inherit Parent class variables 
        self.kilowatts = kilowatts

    def details(self):
        print(f'Your vehicle info is {self.color}, {self.year},{self.make}, {self.model}, with a battery that has {self.kilowatts} kW.')


    def parent_class_year(self):
        print(super().get_year()) # print call is done in the Child Class 

    
    def __add__(self, other):
        return self.kilowatts + other.kilowatts 
    
    def __str__(self):
        return (f'You have a {self.make} {self.model}')


class Bike:

    def __init__(self, frame_weight, alloy_wheels=True):
        self.frame_weight = frame_weight
        self.alloy_wheels = alloy_wheels

    def check_wheels(self):
        if self.alloy_wheels:
            print('This bike has alloy wheels')
        else:
            print('This bike does not have alloy wheels. ')

    def execute(self):
        print('This is from the Bike class')


class Scooter:
    def use_method_from_other_class(self, object_from_class):
        object_from_class.execute() # what matters here is that the object coming from the other class
                                    # has an execute() function (THIS IS DUCK TYPING)


class Skateboard:
    def execute(self):
        print('This is from the Skateboard class ')