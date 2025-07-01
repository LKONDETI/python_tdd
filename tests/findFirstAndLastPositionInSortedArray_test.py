from src.katas.findFirstAndLastPositionInSortedArray import Solution
from unittest import TestCase


class TestFindFirstAndLastPositionInSortedArray (TestCase):

    def test_number_present_in_array(self):
        nums = [5,7,7,8,8,10]
        target = 8
        result = Solution().searchRange(nums, target)
        self.assertEqual(result, [3, 4])
    
    def test_number_not_present_in_array(self):
        nums = [5,7,7,8,8,10]
        target = 6
        result = Solution().searchRange(nums, target)
        self.assertEqual(result, [-1, -1])
        