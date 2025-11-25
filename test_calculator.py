import math
import unittest
from calculator import add, subtract, multiply, divide, sine, tangent

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertIsNone(divide(5, 0))

    def test_sine(self):
        self.assertAlmostEqual(sine(math.pi/2), 1)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(0), 0)

if __name__ == '__main__':
    unittest.main()
