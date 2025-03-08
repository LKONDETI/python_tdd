from src.katas.rottingOranges import Solution
from unittest import TestCase


class TestRottingOranges(TestCase):

    def test_example_1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        solution = Solution()
        self.assertEqual(solution.orangesRotting(grid), 4)
    
    def test_example_2(self):
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        solution = Solution()
        self.assertEqual(solution.orangesRotting(grid), -1)
    
    def test_example_3(self):
        grid = [[0,2]]
        solution = Solution()
        self.assertEqual(solution.orangesRotting(grid), 0)
    