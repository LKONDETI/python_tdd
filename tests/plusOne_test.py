from src.katas.plusOne import Solution
from unittest import TestCase


class TestPlusOne(TestCase):

    def test_three_digits(self):
        digits = [1,2,3]
        output = [1,2,4]
        solution = Solution()
        self.assertEqual(solution.plusOne(digits), output)
    
    def test_four_digits(self):
        digits = [4,3,2,1]
        output = [4,3,2,2]
        solution = Solution()
        self.assertEqual(solution.plusOne(digits), output)
    
    def test_digit_zero(self):
        digits = [0]
        output = [1]
        solution = Solution()
        self.assertEqual(solution.plusOne(digits), output)
    
    def test_digit_nine(self):
        digits = [9]
        output = [1,0]
        solution = Solution()
        self.assertEqual(solution.plusOne(digits), output)