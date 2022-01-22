# Representing Software Engineers
from SoftwareEngineer import Designer
from SoftwareEngineer import Employee
from SoftwareEngineer import SoftwareEngineer
# position, name, age, level, salary

# these represent instances of the Class SoftwareEngineer
se1 = SoftwareEngineer('Jose',25, 7000, 'Junior')
se2 = SoftwareEngineer('Baker', 9, 9000, 'Senior')

print(se1.name)
print(se1.alias)
print(SoftwareEngineer.alias)

se1.code()
se1.code_in_language('Python')
se2.code_in_language('SQL')

#print(se1.information())
print(se1) # without overidding the __str__ method this returns an object 
print(se2)

se3 = SoftwareEngineer('Camila', 8, 9000, 'Senior',)
print(se3 == se2)


# Calling the Class Method
print(SoftwareEngineer.entry_salary(27))

print(se3.level)

designer = Designer('Bella', 8, 1200, 'Houston')
designer.at_studio()
print(designer)
#designer.code() # returns error because designer instance created cannot code 

general = Employee('Tom', 45, 3000)
general.work() # work function from Parent class level 
se1.work() # work function override in the child class level
designer.work()


employees = [se1, se2, se3, general, designer]

#Polymorphism example 
Employee.motivate(employees)

print(se1.salary)

karen = Employee('Karen', 50, 4500)
karen.set_ssn(555555)
print(karen.get_ssn())

se1.code()
print(se1._log_time)
se1.code()
print(se1._log_time)


m = Employee('m', 50, 8000)
m.set_ssn(999999)
print(m.get_ssn())