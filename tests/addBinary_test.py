from unittest import TestCase
from src.katas.addBinary import Solution

class TestAddBinary(TestCase):

    def test_example_1(self):
        a = "11"
        b = "1"
        result = Solution()
        self.assertEqual(result.addBinary(a,b), "100")
    
    def test_example_2(self):
        a = "1010"
        b = "1011"
        result = Solution()
        self.assertEqual(result.addBinary(a,b), "10101")