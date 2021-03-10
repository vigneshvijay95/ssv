import unittest
import calculator
class Testcalc(unittest.TestCase):
    def test_add(self):
        result = calculator.add(10,5)
        self.assertEqual(result,15)
    def test_sub(self):
        result = calculator.sub(10,5)
        self.assertEqual(result,5)
    def test_divide(self):
        result = calculator.divide(100,4)
        self.assertEqual(result, 25)
    def test_multiply(self):
        result = calculator.multiply(100,4)
        self.assertEqual(result, 400)
if __name__ == "__main__":
    unittest.main()
