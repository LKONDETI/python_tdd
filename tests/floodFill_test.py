from src.katas.floodFil import Solution
from unittest import TestCase


class TestFloodFil(TestCase):

    def test_example_1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        color = 2
        output = [[2,2,2],[2,2,0],[2,0,1]]
        solution = Solution()
        self.assertEqual(solution.floodFill(image,sr, sc, color), output)
    
    def test_example_2(self):
        image = [[0,0,0],[0,0,0]]
        sr = 0
        sc = 0
        color = 0
        output = [[0,0,0],[0,0,0]]
        solution = Solution()
        self.assertEqual(solution.floodFill(image,sr, sc, color), output)