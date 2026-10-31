import unittest
from calculator import calculate


class TestCalculator(unittest.TestCase):

    # Addition Tests
    def test_add_positive(self):
        self.assertEqual(calculate(5, 3), 8)

    def test_add_negative(self):
        self.assertEqual(calculate(-5, -3), -8)

    def test_add_mixed(self):
        self.assertEqual(calculate(-5, 3), -2)

    def test_add_zero(self):
        self.assertEqual(calculate(5, 0), 5)

    def test_add_decimal(self):
        self.assertAlmostEqual(calculate(1.5, 2.5), 4.0)

    # Negative Testing
    def test_string_input(self):
        with self.assertRaises(TypeError):
            calculate("5", 2)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            calculate(None, 2)

    def test_boolean_input(self):
        with self.assertRaises(TypeError):
            calculate(True, 2)


if __name__ == "__main__":
    unittest.main()