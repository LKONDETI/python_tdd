from unittest import TestCase
from src.katas.searchInsertPosition import Solution

class TestSearchInsertPosition(TestCase):

    def test_position_5(self):
        nums = [1,3,5,6]
        target = 5
        result = Solution()
        self.assertEqual(result.searchInsert(nums, target), 2)
    
    def test_position_2(self):
        nums = [1,3,5,6]
        target = 2
        result = Solution()
        self.assertEqual(result.searchInsert(nums, target), 1)
    
    def test_position_7(self):
        nums = [1,3,5,6]
        target = 7
        result = Solution()
        self.assertEqual(result.searchInsert(nums, target), 4)