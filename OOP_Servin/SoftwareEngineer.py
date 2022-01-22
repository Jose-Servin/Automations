
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self._ssn = None
        
    def work(self):
        print(f'{self.name} is working')

    def reward(self):
        print(f"Thank you for the hard work {self.name}, here are some free coffee gift cards! ")

    def __str__(self):
        information = f"name: {self.name}, age: {self.age}, salary: {self.salary}"
        return information

    def motivate(employees):
        for i in employees:
            i.reward()

    @property
    def ssn(self):
        return self._ssn

    # setter (allows us to check value, enforce constraints etc)
    @ssn.setter
    def ssn(self, ssn):
        self._ssn = ssn

    @ssn.deleter
    def ssn(self):
        del self._ssn


class SoftwareEngineer(Employee):

    # Class attribute
    alias = 'Keyboard Magician'
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        # these are instance attributes
        self.level = level
        self._log_time = 0

    # this is an instance method
    def code(self):
        print(f"{self.name} is writting code...")
        self._log_time += 1 

    def code_in_language(self, language):
        print (f"{self.name} is writting code in {language}.")

    def work(self):
        print(f'{self.name} is working on some code for Database MGMT')

    def reward(self):
        print(f"Thank you for the hard work {self.name}, here is a new keyboard! ")


    #def information(self):
    #    information = f"name: {self.name}, age: {self.age}, level: {self.level}"
    #    return information

    ###### Python Magic/Dunder Methods #####################

    # __str__ method is used to output all members of the class
    def __str__(self):
        information = f"name: {self.name}, age: {self.age}, salary: {self.salary}, level: {self.level}"
        return information

    # by default __eq__ compares the memory address of an object
    def __eq__(self, other):
        if self.level == other.level:
            if self.salary == other.salary:
                return True
            else:
                return False

    ######## Class Methods ###################################
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        if age < 40:
            return 9000


class Designer(Employee):
    def __init__(self, name, age, salary, studio_location):
        super().__init__(name, age, salary)
        self.studio = studio_location
    
    def at_studio(self):
        print(f"{self.name} is at the studio located in {self.studio}")

    def work(self):
        print(f'{self.name} is working on a new design for the landing page.')

    def __str__(self):
        information = f"name: {self.name}, age: {self.age}, salary: {self.salary}, studio: {self.studio}."
        return information

    def reward(self):
        print(f"Thank you for the hard work {self.name}, here are some new art supplies!")

