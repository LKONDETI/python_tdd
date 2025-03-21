from src.katas.reveseVowelsOfAString import Solution
from unittest import TestCase


class TestReverseVowelsOfAString(TestCase):

    def test_reversing_Icecream(self):
        s = "IceCreAm"
        solution = Solution()
        self.assertEqual(solution.reverseVowels(s), "AceCreIm")
    
    def test_reversing_Leetcode(self):
        s = "leetcode"
        solution = Solution()
        self.assertEqual(solution.reverseVowels(s), "leotcede")