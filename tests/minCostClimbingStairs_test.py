from unittest import TestCase
from src.katas.minCostClimbingStairs import Solution

class TestMinCostClimbingStairs(TestCase):

    def test_when_cost_is_15(self):   
        cost = [10, 15, 20]
        result = Solution()
        self.assertEqual(result.minCostClimbingStairs(cost), 15)
    
    def test_when_cost_is_6(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        result = Solution()
        self.assertEqual(result.minCostClimbingStairs(cost), 6)
    
