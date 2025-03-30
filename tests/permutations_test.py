from src.katas.permutations import Solution
from unittest import TestCase


class TestPermutations(TestCase):

    def test_example_1(self):
        nums = [1, 2, 3]
        output = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
        solution = Solution()
        self.assertEqual(solution.permute(nums), output)
    
    def test_example_2(self):
        nums = [0, 1]
        output = [[1, 0], [0, 1]]
        solution = Solution()
        self.assertEqual(solution.permute(nums), output)
    
    def test_example_3(self):
        nums = [1]
        output = [[1]]
        solution = Solution()
        self.assertEqual(solution.permute(nums), output)