from Employee import Employee

# Reformatting code in PyCharm

# employee_1 = Employee('Jose','Servin',880333,'Analyst', 10000, 0.03, '2021-06-01', None)
# print(employee_1.total_compensation())

all = Employee.instantiate_from_csv()
print(Employee.all_employees)

for employee in Employee.all_employees:
    print(employee.total_compensation())
    print(employee.department)
