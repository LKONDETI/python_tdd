from unittest import TestCase
from src.katas.setMismatch import Solution

class TestSetMismatch(TestCase):

    def test_position_3(self):
        nums = [1,2,2,4]
        result = Solution()
        self.assertEqual(result.findErrorNums(nums), [2,3])
    
    def test_position_2(self):
        nums = [1,1]
        result = Solution()
        self.assertEqual(result.findErrorNums(nums), [1,2])