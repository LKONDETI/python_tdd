from src.katas.searchA2DMatrix2 import Solution
from unittest import TestCase


class TestReverseBits(TestCase):

    def test_target_5(self):
        matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        target = 5
        solution = Solution()
        self.assertEqual(solution.searchMatrix(matrix,target), True)
    
    def test_target_20(self):
        matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        target = 20
        solution = Solution()
        self.assertEqual(solution.searchMatrix(matrix,target), False)

