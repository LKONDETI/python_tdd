from unittest import TestCase
from src.katas.longestCommonPrefix import Solution

class TestLongestCommonSubsequence(TestCase):

    def test_common_string(self):
        strs = ["flower","flow","flight"]
        result = Solution()
        self.assertEqual(result.longestCommonPrefix(strs), "fl")

    def test_no_common_string(self):
        strs = ["dog","racecar","car"]
        result = Solution()
        self.assertEqual(result.longestCommonPrefix(strs), "")
