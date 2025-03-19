from src.katas.surroundedRegions import Solution
from unittest import TestCase


class TestSurroundedRegions(TestCase):

    def test_example_1(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        solution = Solution()
        solution.solve(board) 
        self.assertEqual(board, output)
    
    def test_example_2(self):
        board = [["X"]]
        output = [["X"]]
        solution = Solution()
        solution.solve(board) 
        self.assertEqual(board, output)
    