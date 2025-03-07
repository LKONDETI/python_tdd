from unittest import TestCase
from src.katas.containDuplicate2 import Solution


class TestContainDuplicate2(TestCase):
    def test_check_duplicate_in_array1With4Items(self):
        nums = [1,2,3,1]
        k = 3
        result = Solution()
        self.assertEqual(result.containsNearbyDuplicate(nums,k), True)
    
    def test_check_duplicate_in_array1WithOnes(self):
        nums = [1,0,1,1]
        k = 1
        result = Solution()
        self.assertEqual(result.containsNearbyDuplicate(nums,k), True)
    
    def test_check_duplicate_in_array1WithNoDuplicate(self):
        nums = [1,2,3,1,2,3]
        k = 2
        result = Solution()
        self.assertEqual(result.containsNearbyDuplicate(nums,k), False)
    