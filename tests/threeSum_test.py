#python -m unittest tests/threeSum_test.py
from src.katas.threeSum import Solution
from unittest import TestCase


class TestThreeSum(TestCase):

    def test_ArrayOfSix(self):
        nums = [-1,0,1,2,-1,-4]
        solution = Solution()
        self.assertEqual(solution.threeSum(nums), [[-1,-1,2],[-1,0,1]])

    def test_ArrayOfThree(self):
        nums = [0,1,1]
        solution = Solution()
        self.assertEqual(solution.threeSum(nums), [])

    def test_ArrayOfZeros(self):
        nums = [0,0,0]
        solution = Solution()
        self.assertEqual(solution.threeSum(nums), [[0,0,0]])
    