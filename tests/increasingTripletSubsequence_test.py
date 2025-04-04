from unittest import TestCase
from src.katas.increasingTripletSubsequence import Solution

class TestIncreasingTripletSubsequence(TestCase):

    def test_exaple_1(self):
        nums = [1,2,3,4,5]
        result = Solution()
        self.assertEqual(result.increasingTriplet(nums), True)
    
    def test_example_2(self):
        nums = [5,4,3,2,1]
        result = Solution()
        self.assertEqual(result.increasingTriplet(nums), False)
    
    def test_example_3(self):
        nums = [2,1,5,0,4,6]
        result = Solution()
        self.assertEqual(result.increasingTriplet(nums), True)