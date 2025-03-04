from src.katas.palindromeNumber import Solution
from unittest import TestCase


class TestPalindromeNumber(TestCase):

    def test_positive_value(self):
        nums = 121
        solution = Solution()
        self.assertEqual(solution.isPalindrome(nums), True)
    
    def test_negetive_value(self):
        nums = -121
        solution = Solution()
        self.assertEqual(solution.isPalindrome(nums), False)
    
    def test_four_digits(self):
        nums = 1221
        solution = Solution()
        self.assertEqual(solution.isPalindrome(nums), True)
    
