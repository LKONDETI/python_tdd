from src.katas.longestSubstringWithoutRepeatingChar import Solution
from unittest import TestCase


class TestLongestSubstringWithoutRepeatingChar(TestCase):

    def test_case1(self):
        s = "abcabcbb"
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring(s), 3)
    
    def test_case2(self):
        s = "bbbbb"
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring(s), 1)
    

    def test_case3(self):
        s = "pwwkew"
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring(s), 3)
    
    