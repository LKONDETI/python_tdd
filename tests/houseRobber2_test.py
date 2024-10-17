from unittest import TestCase
from src.katas.houseRobber2 import Solution

class TestHouseRobber2(TestCase):

    def test_for_four_elements(self):
        nums = [1,2,3,1]
        result = Solution()
        self.assertEqual(result.rob(nums), 4)
    
    def test_for_three_elements(self):
        nums = [2,3,2]
        result = Solution()
        self.assertEqual(result.rob(nums), 3)
    
    def test_for_first_three_elements(self):
        nums = [1,2,3]
        result = Solution()
        self.assertEqual(result.rob(nums), 3)
    
    def test_for_random_elements(self):
        nums = [2,7,9,3,1]
        result = Solution()
        self.assertEqual(result.rob(nums), 11)