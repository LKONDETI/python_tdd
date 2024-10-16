from unittest import TestCase
from src.katas.houseRobber import Solution

class TestHouseRobber(TestCase):

    def test_for_four_elements(self):
        nums = [1,2,3,1]
        result = Solution()
        self.assertEqual(result.rob(nums), 4)
    
    def test_for_five_elements(self):
        nums = [2,7,9,3,1]
        result = Solution()
        self.assertEqual(result.rob(nums), 12)