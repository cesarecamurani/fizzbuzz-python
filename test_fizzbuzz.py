import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_should_return_the_number(self):
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(4), 4)
        self.assertEqual(FizzBuzz(7), 7)

    def test_multiple_15_should_return_fizzbuzz(self):
        self.assertEqual(FizzBuzz(45), "fizzbuzz")
        self.assertEqual(FizzBuzz(30), "fizzbuzz")
        self.assertEqual(FizzBuzz(60), "fizzbuzz")

if __name__ == '__main__':
    unittest.main()
