from unittest import TestCase
from src.katas.longestSubarrayOf1AfterDelOneElement import Solution

class TestLongestSubarrayOf1AfterDelOneElement(TestCase):

    def test_example_1(self):
        nums = [1,1,0,1]
        result = Solution()
        self.assertEqual(result.longestSubarray(nums), 3)
    
    def test_example_2(self):
        nums = [0,1,1,0,1]
        result = Solution()
        self.assertEqual(result.longestSubarray(nums), 3)
    
    def test_example_3(self):
        nums = [1,1,1]
        result = Solution()
        self.assertEqual(result.longestSubarray(nums), 2)
    
    def test_example_4(self):
        nums = [0,1,1,1,0,1,1,0,1]
        result = Solution()
        self.assertEqual(result.longestSubarray(nums), 5)
