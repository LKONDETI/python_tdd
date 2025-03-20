from src.katas.maxNumberOfKSumPairs import Solution
from unittest import TestCase


class TestmaxNunberOfKSumPairs(TestCase):

    def test_example1(self):
        nums = [1,2,3,4]
        k = 5
        solution = Solution()
        self.assertEqual(solution.maxOperations(nums,k), 2)
    
    def test_example2(self):
        nums = [3,1,3,4,3]
        k = 6
        solution = Solution()
        self.assertEqual(solution.maxOperations(nums,k), 1)