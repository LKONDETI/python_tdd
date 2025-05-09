from unittest import TestCase
from src.katas.rotateArray import Solution

class TestRotateArray(TestCase):

    def test_example_1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        output = [5,6,7,1,2,3,4]
        result = Solution()
        self.assertEqual(result.rotate(nums,k), output)
    
    def test_example_2(self):
        nums = [-1,-100,3,99]
        k = 2
        output = [3,99,-1,-100]
        result = Solution()
        self.assertEqual(result.rotate(nums,k), output)
    
    def test_two_items(self):
        nums = [1,2]
        k = 3
        output = [2,1]
        result = Solution()
        self.assertEqual(result.rotate(nums,k), output)
    