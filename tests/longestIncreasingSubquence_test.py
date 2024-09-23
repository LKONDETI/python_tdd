from unittest import TestCase
from src.katas.longestIncreasingSubquence import Solution

class TestLongestIncreasingSubquence(TestCase):

    def test_first_four_natural_numbers(self):
        nums = [1,2,4,3]
        result = Solution()
        self.assertEqual(result.lengthOfLIS(nums), 3)
    
    def test_Example_1(self):
        nums = [10,9,2,5,3,7,101,18]
        result = Solution()
        self.assertEqual(result.lengthOfLIS(nums), 4)

    def test_Example_2(self):
        nums = [0,1,0,3,2,3]
        result = Solution()
        self.assertEqual(result.lengthOfLIS(nums), 4)

    def test_Example_3(self):
        nums = [7,7,7,7,7,7,7]
        result = Solution()
        self.assertEqual(result.lengthOfLIS(nums), 1)
