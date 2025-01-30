from unittest import TestCase
from src.katas.KthLargestElement import Solution

class TestHouseRobber(TestCase):

    def test_case1(self):
        nums = [3,2,1,5,6,4]
        k = 2
        result = Solution()
        self.assertEqual(result.findKthLargest(nums, k ), 5)
    
    def test_case2(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        result = Solution()
        self.assertEqual(result.findKthLargest(nums, k ), 4)