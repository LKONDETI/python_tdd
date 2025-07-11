from unittest import TestCase
from src.katas.minSizeSubarraySum import Solution

class TestMinimumSizeSubarraySum(TestCase):

    def test_target_7(self):
        nums = [2,3,1,2,4,3]
        target = 7
        result = Solution()
        self.assertEqual(result.minSubArrayLen(target,nums), 2)
    
    def test_target_4(self):
        nums = [1,4,4]
        target = 4
        result = Solution()
        self.assertEqual(result.minSubArrayLen(target,nums), 1)
    
    def test_target_not_in_list(self):
        nums = [1,1,1,1,1,1,1,1]
        target = 11
        result = Solution()
        self.assertEqual(result.minSubArrayLen(target,nums), 0)