from unittest import TestCase
from src.katas.contiquousArray import Solution

class TestCoinsChange(TestCase):

    def test_three_elements(self):
        nums = [0,1,0]
        result = Solution()
        self.assertEqual(result.findMaxLength(nums), 2)
    

    def test_two_elements(self):
        nums = [0,1]
        result = Solution()
        self.assertEqual(result.findMaxLength(nums), 2)