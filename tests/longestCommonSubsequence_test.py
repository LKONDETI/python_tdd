from unittest import TestCase
from src.katas.longestCommonSubsequence import Solution

class TestLongestCommonSubsequence(TestCase):

    def test_example_1(self):
        text1 = "abcde"
        text2 = "ace"
        result = Solution()
        self.assertEqual(result.longestCommonSubsequence(text1,text2), 3)
    
    def test_example_2(self):
        text1 = "abc"
        text2 = "abc"
        result = Solution()
        self.assertEqual(result.longestCommonSubsequence(text1,text2), 3)
    
    def test_example_3(self):
        text1 = "abc"
        text2 = "def"
        result = Solution()
        self.assertEqual(result.longestCommonSubsequence(text1,text2), 0)