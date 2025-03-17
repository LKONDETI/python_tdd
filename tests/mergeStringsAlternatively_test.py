from unittest import TestCase
from src.katas.mergeStringsAlternatively import Solution

class TestMergeStringsAlternatively(TestCase):

    def test_example_1(self):
        word1 = "abc"
        word2 = "pqr"
        result = Solution()
        self.assertEqual(result.mergeAlternately(word1, word2), "apbqcr")
    
    def test_example_2(self):
        word1 = "abcd"
        word2 = "pq"
        result = Solution()
        self.assertEqual(result.mergeAlternately(word1, word2), "apbqcd")
    
    