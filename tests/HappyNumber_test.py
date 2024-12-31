from unittest import TestCase
from src.katas.happyNumber import Solution

class TestHappyNumber(TestCase):

    def test_n_is_True(self):
        n = 19
        result = Solution()
        self.assertEqual(result.isHappy(n), True)
    
    def test_single_digit_2(self):
        n = 2
        result = Solution()
        self.assertEqual(result.isHappy(n), False)
    