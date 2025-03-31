from src.katas.subsets import Solution
from unittest import TestCase


class TestSubsets(TestCase):

    def test_example_1(self):
        nums = [1, 2, 3]
        output = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
        solution = Solution()
        self.assertEqual(solution.subsets(nums), output)
    
    def test_example_2(self):
        nums = [0]
        output = [[0], []]
        solution = Solution()
        self.assertEqual(solution.subsets(nums), output)
    
    def test_example_3(self):
        nums = [1, 2]
        output = [[1, 2], [1], [2], []]
        solution = Solution()
        self.assertEqual(solution.subsets(nums), output)