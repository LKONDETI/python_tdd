from unittest import TestCase
from src.katas.rotateArray import Solution

class TestRotateArray(TestCase):

    def test_example_1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        output = [5,6,7,1,2,3,4]
        result = Solution()
        self.assertEqual(result.rotate(nums,k), output)
    