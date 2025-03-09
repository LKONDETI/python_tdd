from unittest import TestCase
from src.katas.findtheIndexOfTheFirstOccuranceInAString import Solution

class TestFindTheIndexOfTheFirstOccuranceInAString(TestCase):
    
    def test_example_1(self):
        haystack = "sadbutsad"
        needle = "sad"
        result = Solution()
        self.assertEqual(result.strStr(haystack, needle), 0)
    
    def test_example_2(self):
        haystack = "leetcode"
        needle = "leeto"
        result = Solution()
        self.assertEqual(result.strStr(haystack, needle), -1)
    

    