from src.katas.sqrt_x import Solution
from unittest import TestCase


class TestSqrt_x(TestCase):

    def test_perfect_square(self):
        x = 4
        solution = Solution()
        self.assertEqual(solution.mySqrt(x), 2)
    
    def test_non_perfect_square(self):
        x = 8
        solution = Solution()
        self.assertEqual(solution.mySqrt(x), 2)