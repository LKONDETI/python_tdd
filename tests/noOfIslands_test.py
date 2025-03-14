from src.katas.noOfIslands import Solution
from unittest import TestCase


class TestNumberOfIslands(TestCase):

    def test_example_1(self):
        grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        solution = Solution()
        self.assertEqual(solution.numIslands(grid), 1)

    def test_example_2(self):
        grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        solution = Solution()
        self.assertEqual(solution.numIslands(grid), 3)