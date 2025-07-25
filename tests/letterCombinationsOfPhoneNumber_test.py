from unittest import TestCase
from src.katas.letterCombinationsOfPhoneNumber import Solution

class TestLetterCombinationsOfPhoneNumber(TestCase):

    def test_digits_23(self):
        n = "23"
        result = Solution()
        self.assertEqual(result.letterCombinations(n), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
    
    def test_digits_2(self):
        n = "2"
        result = Solution()
        self.assertEqual(result.letterCombinations(n), ["a","b","c"])
    
    def test_digits_empty(self):
        n = ""
        result = Solution()
        self.assertEqual(result.letterCombinations(n), [])