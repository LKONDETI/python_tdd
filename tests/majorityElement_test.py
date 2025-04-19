from unittest import TestCase
from src.katas.majorityElement import Solution

class TestMajorityElement(TestCase):

    def test_example_1(self):
        nums = [3,2,3]
        result = Solution()
        self.assertEqual(result.majorityElement(nums), 3)
    
    def test_example_2(self):
        nums = [2,2,1,1,1,2,2]
        result = Solution()
        self.assertEqual(result.majorityElement(nums), 2)
    