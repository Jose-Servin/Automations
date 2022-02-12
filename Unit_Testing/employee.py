import requests

class Employee:
    """A simple employee classed used for unit testing"""
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'https://company.com/{self.last_name}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

