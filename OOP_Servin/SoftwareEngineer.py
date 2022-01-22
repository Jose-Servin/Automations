
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

class SoftwareEngineer():

    # Class attribute
    alias = 'Keyboard Magician'
    def __init__(self, name, age, level, salary):
        # these are instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # this is an instance method
    def code(self):
        print(f"{self.name} is writting code...")

    def code_in_language(self, language):
        print (f"{self.name} is writting code in {language}.")

    #def information(self):
    #    information = f"name: {self.name}, age: {self.age}, level: {self.level}"
    #    return information

    ###### Python Magic/Dunder Methods #####################

    # __str__ method is used to output all members of the class
    def __str__(self):
        information = f"name: {self.name}, age: {self.age}, level: {self.level}"
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