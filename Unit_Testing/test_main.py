import unittest
import main


class TestMain(unittest.TestCase):  # inherit testing capabilities from unittest module

    def test_add(self):
        self.assertEqual(main.add(10, 5), 15)  # Normal addition between two positive numbers
        self.assertEqual(main.add(-5, 10), 5)  # Edge case: adding a negative plus positive number
        self.assertEqual(main.add(-4, -1), -5)  # Edge Case: adding two negative numbers

    def test_subtract(self):
        self.assertEqual(main.subtract(10, 5), 5)  # Normal subtraction between two positive numbers
        self.assertEqual(main.subtract(-5, 10), -15)  # Edge case: subtraction a negative plus positive number
        self.assertEqual(main.subtract(-4, -1), -3)  # Edge Case: subtraction two negative numbers

    def test_multiply(self):
        self.assertEqual(main.multiply(10, 5), 50)  # Normal multiplying between two positive numbers
        self.assertEqual(main.multiply(-5, 10), -50)  # Edge case: multiplying a negative plus positive number
        self.assertEqual(main.multiply(-4, -1), 4)  # Edge Case: multiplying two negative numbers

    def test_divide(self):
        self.assertEqual(main.divide(10, 5), 2)  # Normal dividing between two positive numbers
        self.assertEqual(main.divide(-10, 5), -2)  # Edge case: dividing a negative plus positive number
        self.assertEqual(main.divide(-4, -1), 4)  # Edge Case: dividing two negative numbers
        self.assertEqual(main.divide(5, 2), 2.5)  # New Edge Case to catch floor division after finding bug in code

        self.assertRaises(ValueError, main.divide, 10, 0)  # Method 1: testing exceptions

        with self.assertRaises(ValueError):  # Method 2: testing exceptions with context manager
            main.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
