import csv 
import pandas as pd

class Employee:

    all_employees = []

    def __init__(self, first_name, last_name, ID, department, salary, bonus, start_date, end_date = None):
        self.first_name  = first_name
        self.last_name = last_name
        self.ID = ID
        self.department = department
        self.salary = salary
        self.bonus = bonus
        self.start_date = start_date
        self.end_date = end_date

        Employee.all_employees.append(self)

    def total_compensation(self):
        return self.salary + (self.salary * self.bonus) 

    def __str__(self):
        return f""" 
        Employee Report: \n
        First Name: {self.first_name}
        Last Name: {self.last_name}
        ID: {self.ID}
        Department: {self.department}
        Salary: {self.salary}
        Bonus: {self.bonus} 
        Start Date: {self.start_date} 
        End Date: {self.end_date} 
        
        """

    def __repr__(self):
        return f""" 
        Employee Report: 
        \t First Name: {self.first_name} 
        \t Last Name: {self.last_name}
        \t ID: {self.ID} 
        \t Department: {self.department}
        \t Salary: {self.salary}
        \t Bonus: {self.bonus}
        \t Start Date: {self.start_date}
        \t End Date: {self.end_date} 
        
        """




    @classmethod
    def instantiate_from_csv(cls):
        with open('/Users/joseservin/Automations/OOP_Servin/employees.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Employee(
                first_name=item.get('first_name'),
                last_name=item.get('last_name'),
                ID=int(item.get('ID')),
                department= item.get('Department'),
                salary = int(item.get('Salary')),
                bonus = float(item.get('bonus')),
                start_date = pd.to_datetime(item.get('start_date')),
                end_date = pd.to_datetime(item.get('end_date'))

            )



class Analyst(Employee):
    def __init__(self, first_name, last_name, ID, department, salary, bonus, start_date, end_date =  None):
        super().__init__(first_name, last_name, ID, department, salary, bonus, start_date, end_date)

class Sales(Employee):
    def __init__(self, first_name, last_name, ID, department, salary, bonus, start_date, end_date=None):
        super().__init__(first_name, last_name, ID, department, salary, bonus, start_date, end_date)

class HR(Employee):
    def __init__(self, first_name, last_name, ID, department, salary, bonus, start_date, end_date=None):
        super().__init__(first_name, last_name, ID, department, salary, bonus, start_date, end_date)

