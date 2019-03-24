import unittest

# Write a function that takes two arguments and returns all numbers which are divisible by a given divisor.
# The first argument is an array of numbers and the second is the divisor.

def divisible_by(numbers, divisor):
    return [x for x in numbers if x%divisor == 0]

class MyTest(unittest.TestCase):
    def test_divisible_by(self):
        self.assertEqual(divisible_by([1, 2, 3, 4, 5, 6], 3), [3, 6])

if __name__ == '__main__':
    unittest.main()
