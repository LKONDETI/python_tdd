from src.katas.removeDuplicatesFromSortedArray import Solution
from unittest import TestCase


class TestRemoveDuplicatesFromSortedArray(TestCase):

    def test_two_integers(self):
        nums = [1, 1, 2]
        solution = Solution()
        self.assertEqual(solution.removeDuplicates(nums), 2)
    
    def test_multiple_integers(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        solution = Solution()
        self.assertEqual(solution.removeDuplicates(nums), 5)

    def test_umique_integers(self):
        nums = [1, 2, 3, 4, 5]
        solution = Solution()
        self.assertEqual(solution.removeDuplicates(nums), 5)