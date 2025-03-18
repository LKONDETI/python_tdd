from unittest import TestCase
from src.katas.greatestCommonDivisorofStrings import Solution

class TestGreatestCommonDivisorofStrings(TestCase):

    def test_example_1(self):
        str1 = "ABCABC"
        str2 = "ABC"
        result = Solution()
        self.assertEqual(result.gcdOfStrings(str1,str2), "ABC")
    
    def test_example_2(self):
        str1 = "ABABAB"
        str2 = "ABAB"
        result = Solution()
        self.assertEqual(result.gcdOfStrings(str1,str2), "AB")
    
    def test_example_3(self):
        str1 = "LEET"
        str2 = "CODE"
        result = Solution()
        self.assertEqual(result.gcdOfStrings(str1,str2), "")
    