# Representing Software Engineers
from curses.ascii import SO
from re import S
from SoftwareEngineer import SoftwareEngineer
# position, name, age, level, salary

# these represent instances of the Class SoftwareEngineer
se1 = SoftwareEngineer('Jose',25,'Junior', 7000)
se2 = SoftwareEngineer('Baker', 9, 'Senior', 9000)

print(se1.name)
print(se1.alias)
print(SoftwareEngineer.alias)

se1.code()
se1.code_in_language('Python')
se2.code_in_language('SQL')

#print(se1.information())
print(se1) # without overidding the __str__ method this returns an object 
print(se2)

se3 = SoftwareEngineer('Camila', 8, 'Senior', 10000)
print(se3 == se2)


# Calling the Class Method
print(SoftwareEngineer.entry_salary(27))