from src.katas.jumpGame2 import Solution
from unittest import TestCase


class TestJumpGame2(TestCase):

    def test_output_1(self):
        nums = [2,3,1,1,4]
        solution = Solution()
        self.assertEqual(solution.jump(nums), 2)
    
    def test_output_2(self):
        nums = [2,3,0,1,4]
        solution = Solution()
        self.assertEqual(solution.jump(nums), 2)