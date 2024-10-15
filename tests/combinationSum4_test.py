from unittest import TestCase
from src.katas.combinationSum4 import Solution

class TestCombinationSum4(TestCase):

    def test_single_item(self):
        nums = [9]
        result = Solution()
        self.assertEqual(result.combinationSum4(nums, 3), 0)
    
    def test_three_items(self):
        nums = [1,2,3]
        result = Solution()
        self.assertEqual(result.combinationSum4(nums, 4), 7)

