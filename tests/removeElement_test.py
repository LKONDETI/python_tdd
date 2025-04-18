from unittest import TestCase
from src.katas.removeElement import Solution

class TestRemoveElement(TestCase):

    def test_two_integers(self):
        nums = [3, 2, 2, 3]
        val = 3
        result = Solution()
        self.assertEqual(result.removeElement(nums,val), 2)
    
    def test_four_integers(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        result = Solution()
        self.assertEqual(result.removeElement(nums,val), 5)
    
    def test_empty_list(self):
        nums = []
        val = 0
        result = Solution()
        self.assertEqual(result.removeElement(nums,val), 0)
    
    def test_unique_integer(self):
        nums = [1,2,4,3,5]
        val = 2
        result = Solution()
        self.assertEqual(result.removeElement(nums,val), 4)