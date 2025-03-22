from src.katas.maximumNumberOfVowelsinASubstringOfGivenLength import Solution
from unittest import TestCase


class TestMaximumNumberOfVowelsinASubstringOfGivenLength(TestCase):

    def test_example_1(self):
        s = "abciiidef"
        k = 3
        solution = Solution()
        self.assertEqual(solution.maxVowels(s,k), 2)
    
    def test_example_2(self):
        s = "aeiou"
        k = 2
        solution = Solution()
        self.assertEqual(solution.maxVowels(s,k), 2)
    
    def test_example_3(self):
        s = "leetcode"
        k = 3
        solution = Solution()
        self.assertEqual(solution.maxVowels(s,k), 2)
    