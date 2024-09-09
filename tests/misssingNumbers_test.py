from src.katas.missingNumber import Solution
from unittest import TestCase


class TestNumberOfOneBit(TestCase):

    def test_array_of_three(self):
        nums = [1,0,3]
        solution = Solution()
        self.assertEqual(solution.missingNumber(nums), 2)

    def test_array_of_two(self):
        nums = [0,1]
        solution = Solution()
        self.assertEqual(solution.missingNumber(nums), 2)

    def test_array_of_eight(self):
        nums = [9,6,4,2,3,5,7,0,1]
        solution = Solution()
        self.assertEqual(solution.missingNumber(nums), 8)

