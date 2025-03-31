from unittest import TestCase
from src.katas.findTheDifferenceOfTwoArrays import Solution

class TestFindTheDifferenceOfTwoArrays(TestCase):

    def test_input_with_one_duplicate(self):
        nums1 = [1,2,3]
        nums2 = [2,4,6]
        output = [[1,3],[4,6]]
        result = Solution()
        self.assertEqual(result.findDifference(nums1, nums2), output)
    
    def test_input_with_duplicate_arrays(self):
        nums1 = [1,2,3,3]
        nums2 = [1,1,2,2]
        output = [[3],[]]
        result = Solution()
        self.assertEqual(result.findDifference(nums1, nums2), output)
    
    def test_same_arrays(self):
        nums1 = [1,2,3]
        nums2 = [1,2,3]
        output = [[],[]]
        result = Solution()
        self.assertEqual(result.findDifference(nums1, nums2), output)
    