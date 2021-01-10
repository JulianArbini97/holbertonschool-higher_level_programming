#!/usr/bin/python3
import unittest
"""
unittest for mas integer
"""
max_integer = __import__('6-max_integer').max_integer


class testing(unittest.TestCase):
    """ function to test cases"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([23, 48, 57, 128]), 128)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -56, -20]), -1)
        self.assertEqual(max_integer([3, 3.2, 3.3]), 3.3)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 4, 3]), 4)
        v = 1
        self.assertEqual(max_integer([v, 3]), 3)


if __name__ == "__main__":
    unittest.main()
