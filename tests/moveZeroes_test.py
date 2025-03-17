from unittest import TestCase
from src.katas.moveZeroes import Solution

class TestMergeStringsAlternatively(TestCase):

    def test_example_1(self):
        nums = [0,1,0,3,12]
        result = Solution()
        self.assertEqual(result.moveZeroes(nums), [1,3,12,0,0])
    
    def test_example_2(self):
        nums = [0]
        result = Solution()
        self.assertEqual(result.moveZeroes(nums), [0])
    