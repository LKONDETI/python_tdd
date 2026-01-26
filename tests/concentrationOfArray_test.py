from src.katas.concatenationOfArray import Solution
from unittest import TestCase


class TestConcatenationOfArray(TestCase):

    def test_case1(self):
        nums = [1,2,1]
        solution = Solution()
        self.assertEqual(solution.getConcatenation(nums), [1,2,1,1,2,1])
    
    def test_case2(self):
        nums = [1,3,2,1]
        solution = Solution()
        self.assertEqual(solution.getConcatenation(nums), [1,3,2,1,1,3,2,1])