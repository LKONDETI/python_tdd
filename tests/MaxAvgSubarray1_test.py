from unittest import TestCase
from src.katas.maximumAverageSubarray1 import Solution

class TestmaximumAverageSubarray(TestCase):
    
    def test_case1(self):
        nums = [1,12,-5,-6,50,3]
        result = Solution()
        self.assertEqual(result.findMaxAverage(nums, 4), 12.75000)
    
    def test_case2(self):
        nums = [5]
        result = Solution()
        self.assertEqual(result.findMaxAverage(nums, 1), 5.00000)
    