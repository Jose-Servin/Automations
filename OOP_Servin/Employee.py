class Employee:

    def __init__(self, first_name, last_name, ID, department, salary, bonus, start_date, end_date:None):
        self.first_name  = first_name
        self.last_name = last_name
        self.ID = ID
        self.department = department
        self.salary = salary
        self.bonus = bonus
        self.start_date = start_date
        self.end_date = end_date

    def total_compensation(self):
        return self.salary + (self.salary * self.bonus) 
