from unittest import TestCase
from src.katas.determineIfTwoStringsAreClose import Solution

class TestDetermineIfTwoStringsAreClose (TestCase):

    def test_example_1(self):
        word1 = "abc"
        word2 = "bca"
        result = Solution()
        self.assertEqual(result.closeStrings(word1,word2), True)
    
    def test_example_2(self):
        word1 = "a"
        word2 = "aa"
        result = Solution()
        self.assertEqual(result.closeStrings(word1,word2), False)
    
    def test_example_3(self):
        word1 = "cabbba"
        word2 = "abbccc"
        result = Solution()
        self.assertEqual(result.closeStrings(word1,word2), True)