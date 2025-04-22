from src.katas.wordPattern import Solution
from unittest import TestCase


class TestWordPattern(TestCase):

    def test_abba(self):
        pattern = "abba"
        s = "dog cat cat dog"
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern,s), True)
    
    def test_abca(self):
        pattern = "abca"
        s = "dog cat dog fish"
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern,s), False)
    
    def test_empty_string(self):
        pattern = ""
        s = ""
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), True)
    
    def test_aaaa(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), False)