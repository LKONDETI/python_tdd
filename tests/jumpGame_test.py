from src.katas.jumpGame import Solution
from unittest import TestCase


class TestJumpGame(TestCase):

    def test_output_1(self):
        nums = [2,3,1,1,4]
        solution = Solution()
        self.assertEqual(solution.canJump(nums), True)
    
    def test_output_2(self):
        nums = [3,2,1,0,4]
        solution = Solution()
        self.assertEqual(solution.canJump(nums), False)