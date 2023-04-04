import unittest

from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci()

    def test_fibonacci_with_positive_number(self):
        self.assertEqual(self.fib(9), 34)

    def test_fibonacci_with_negative_number(self):
        with self.assertRaises(ValueError):
            self.fib(-1)

    def test_fibonacci_with_zero(self):
        self.assertEqual(self.fib(0), 0)

    def test_fibonacci_with_float_number(self):
        with self.assertRaises(ValueError):
            self.fib(.5)

    def test_fibonacci_with_string(self):
        with self.assertRaises(ValueError):
            self.fib("abc")

    def test_fibonacci_with_empty_list(self):
        with self.assertRaises(ValueError):
            self.fib([])

    def test_fibonacci_cache(self):
        self.fib(10)
        self.assertEqual(self.fib.cache, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
