from unittest import TestCase
from src.katas.nthTribonacciNumber import Solution

class TestNthTribonacciNumber(TestCase):

    def test_n_4(self):
        n = 4
        result = Solution()
        self.assertEqual(result.tribonacci(n), 4)
    
    def test_n_25(self):
        n = 25
        result = Solution()
        self.assertEqual(result.tribonacci(n), 1389537)
