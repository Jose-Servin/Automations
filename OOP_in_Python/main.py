
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

    
    class Insurance:
        def __init__(self, company='StateFarm', rate=165):
            self.company = company
            self.rate = rate

        def show_info(self):
            print(f'Your insurance company is {self.company} and you pay ${self.rate} per month.')

