import unittest
from unittest.mock import patch  # patch can be used as decorator or context manager
from employee import Employee


# Real world application of unit testing a OOP project

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp for each test')
        self.emp1 = Employee('Jose', 'Servin', 5000)
        self.emp2 = Employee('Baker', 'Servin', 3000)

    def tearDown(self) -> None:
        print('tearDown for each test')

    def test_email(self):
        print('testing_email')
        self.assertEqual(self.emp1.email, 'Jose.Servin@email.com')
        self.assertEqual(self.emp2.email, 'Baker.Servin@email.com')

        self.emp1.first_name = 'Kike'
        self.emp2.first_name = 'GoodBoy'

        self.assertEqual(self.emp1.email, 'Kike.Servin@email.com')
        self.assertEqual(self.emp2.email, 'GoodBoy.Servin@email.com')

    def test_fullname(self):
        print('testing full_name')
        self.assertEqual(self.emp1.fullname, 'Jose Servin')
        self.assertEqual(self.emp2.fullname, 'Baker Servin')

        self.emp1.first_name = 'Kike'
        self.emp2.first_name = 'GoodBoy'

        self.assertEqual(self.emp1.fullname, 'Kike Servin')
        self.assertEqual(self.emp2.fullname, 'GoodBoy Servin')

    def test_apply_raise(self):
        print('testing apply_raise method')
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 5250)
        self.assertEqual(self.emp2.pay, 3150)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:  # mocking the requests.get from employee module
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('March')
            mocked_get.assert_called_with('https://company.com/Servin/March')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp1.monthly_schedule('April')
            mocked_get.assert_called_with('https://company.com/Servin/April')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
