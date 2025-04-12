from src.katas.findPivotIndex import Solution
from unittest import TestCase


class TestFindPivotIndex(TestCase):

    def test_solution_3(self):
        nums = [1,7,3,6,5,6]
        solution = Solution()
        self.assertEqual(solution.pivotIndex(nums), 3)
    
    def test_solution_1(self):
        nums = [1,2,3]
        solution = Solution()
        self.assertEqual(solution.pivotIndex(nums), -1)
    
    def test_solution_0(self):
        nums = [2,1,-1]
        solution = Solution()
        self.assertEqual(solution.pivotIndex(nums), 0)
    
   