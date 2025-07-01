from unittest import TestCase
from src.katas.longestPalindromeSubstring import Solution

class TestLongestPalindromeSubstring (TestCase):

    def test_bab(self):
        s = "babad"
        result = Solution()
        self.assertEqual(result.longestPalindrome(s), "bab")
    
    def test_cbbd(self):
        s = "cbbd"
        result = Solution()
        self.assertEqual(result.longestPalindrome(s), "bb")