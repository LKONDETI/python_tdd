from unittest import TestCase
from src.katas.maxConsecutiveOnes import Solution

class TestmaxConsecutiveOnes(TestCase):
    
    def test_case1(self):
        nums = [1,1,0,1,1,1]
        result = Solution()
        self.assertEqual(result.findMaxConsecutiveOnes(nums), 3)
    def test_case2(self):
        nums = [1,0,1,1,0,1]
        result = Solution()
        self.assertEqual(result.findMaxConsecutiveOnes(nums), 2)