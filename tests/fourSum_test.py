from src.katas.fourSum import Solution
from unittest import TestCase


class TestFourSum(TestCase):

    def test_example_1(self):
        nums = [1,0,-1,0,-2,2]
        target = 0
        output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        solution = Solution()
        self.assertEqual(solution.fourSum(nums,target), output)
    
    def test_example_2(self):
        nums = [2,2,2,2,2]
        target = 8
        output = [[2,2,2,2]]
        solution = Solution()
        self.assertEqual(solution.fourSum(nums,target), output)
    
    def test_example_3(self):
        nums = [0,0,0,0]
        target = 0
        output = [[0,0,0,0]]
        solution = Solution()
        self.assertEqual(solution.fourSum(nums,target), output)
