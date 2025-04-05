from src.katas.singleNumber import Solution
from unittest import TestCase


class TestSingleNumber(TestCase):

    def test_three_prositive_integers(self):
        nums = [2,2,1]
        solution = Solution()
        self.assertEqual(solution.singleNumber(nums), 1)
    
    def test_five_integers(self):
        nums = [4,1,2,1,2]
        solution = Solution()
        self.assertEqual(solution.singleNumber(nums), 4)
    
    def test_single_integer(self):
        nums = [1]
        solution = Solution()
        self.assertEqual(solution.singleNumber(nums), 1)
    