from src.katas.partitionEqualSubsetSum import Solution
from unittest import TestCase


class TestPartitionEqualSubsetSum(TestCase):

    def test_example_1(self):
        nums = [1,5,11,5]
        solution = Solution()
        self.assertEqual(solution.canPartition(nums), True)
    
    def test_example_2(self):
        nums = [1,2,3,5]
        solution = Solution()
        self.assertEqual(solution.canPartition(nums), False)