import unittest
import sv
class TestSum(unittest.TestCase):
    def setUp(self):
        self.a=10
        self.b=20
    def test_sum(self):
        result = sv.sum(self.a,self.b)
        self.assertEqual(result,30)
if __name__ == "__main__":
    unittest.main()