from src.katas.equalRowAndColumnPair import Solution
from unittest import TestCase


class TestEqualRowAndColumnPair(TestCase):

    def test_single_pair(self):
        grid = [[3,2,1],[1,7,6],[2,7,7]]
        solution = Solution()
        self.assertEqual(solution.equalPairs(grid), 1)
    
    def test_multiple_pairs(self):
        grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
        solution = Solution()
        self.assertEqual(solution.equalPairs(grid), 3)
 