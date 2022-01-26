class Car:
    # idea behind __init__ is that this method will get called once automatically per object 
    def __init__(self, color, year, make, model ): # grey 2021 Honda Accord 
        self.color = color
        self.year = year
        self.make = make
        self.model = model

    def details(self):
        print(f'Your vehicle info is {self.color}, {self.year}, {self.make}, {self.model}.')



