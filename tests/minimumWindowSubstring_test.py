from unittest import TestCase
from src.katas.minimumWindowSubstring import Solution

class TestMinimumWindowSubstring(TestCase):

    def test_case1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        result = Solution()
        self.assertEqual(result.minWindow(s,t), "BANC")
    
    def test_case2(self):
        s = "a"
        t = "a"
        result = Solution()
        self.assertEqual(result.minWindow(s,t), "a")
    
    def test_case3(self):
        s = "a"
        t = "aa"
        result = Solution()
        self.assertEqual(result.minWindow(s,t), "")
    
