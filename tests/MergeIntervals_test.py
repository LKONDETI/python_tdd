from src.katas.MergeIntervals import Solution
from unittest import TestCase


class TestThreeSum(TestCase):

    def test_case1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        solution = Solution()
        self.assertEqual(solution.merge(intervals), [[1,6],[8,10],[15,18]])
    
    def test_case2(self):
        intervals = [[1,4],[4,5]]
        solution = Solution()
        self.assertEqual(solution.merge(intervals), [[1,5]])