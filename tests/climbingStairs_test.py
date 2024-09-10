from unittest import TestCase
from src.katas.climbingStairs import Solution

class TestClimbingStairs(TestCase):

    def test_when_n_is_two(self):
        n = 2
        result = Solution()
        self.assertEqual(result.climbStairs(n), 2)
    
    def test_when_n_is_three(self):
        n = 3
        result = Solution()
        self.assertEqual(result.climbStairs(n), 3)
    
    def test_when_n_is_five(self):
        n = 5
        result = Solution()
        self.assertEqual(result.climbStairs(n), 8)
    
    def test_when_n_is_hundred(self):
        n = 100
        result = Solution()
        self.assertEqual(result.climbStairs(n), 573147844013817084101)