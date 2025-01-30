from src.katas.NextGreaterElement1 import Solution
from unittest import TestCase


class TestNextGreaterElement1(TestCase):

    def test_array_of_three(self):
        nums1 = [4,1,2]
        nums2 = [1,3,4,2]
        res = [-1,3,-1]
        solution = Solution()
        self.assertEqual(solution.nextGreaterElement(nums1,nums2), res)
    
    def test_array_of_two(self):
        nums1 = [2,4]
        nums2 = [1,2,3,4]
        res = [3,-1]
        solution = Solution()
        self.assertEqual(solution.nextGreaterElement(nums1,nums2), res)
    