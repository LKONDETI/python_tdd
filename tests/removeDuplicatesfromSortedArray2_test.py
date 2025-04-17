from unittest import TestCase
from src.katas.removeDuplicatesFromSortedArray2 import Solution

class TestRemoveDuplicatesFromSortedArray2(TestCase):

    def test_three_integers(self):
        nums = [1,1,1,2,2,3]
        result = Solution()
        self.assertEqual(result.removeDuplicates(nums), 5)

    def test_multiple_repeated_integers(self):
        nums = [0,0,1,1,1,1,2,3,3]
        result = Solution()
        self.assertEqual(result.removeDuplicates(nums), 7)