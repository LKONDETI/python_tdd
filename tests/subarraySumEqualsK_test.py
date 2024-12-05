from src.katas.subarraySumEqualsK import Solution
from unittest import TestCase


class TestSubarraySumEqualsK(TestCase):

    def test_three_ones(self):
        nums = [1,1,1]
        solution = Solution()
        self.assertEqual(solution.subarraySum(nums,2), 2)
    
    def test_three_different_integers(self):
        nums = [1,2,3]
        solution = Solution()
        self.assertEqual(solution.subarraySum(nums,3), 2)
