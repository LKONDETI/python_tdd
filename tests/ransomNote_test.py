from src.katas.ransomNote import Solution
from unittest import TestCase


class TestRansomNote(TestCase):

    def test_example_1(self):
        ransomNote = "a"
        magazine = "b"
        solution = Solution()
        self.assertEqual(solution.canConstruct(ransomNote, magazine), False)
    
    def test_example_2(self):
        ransomNote = "aa"
        magazine = "ab"
        solution = Solution()
        self.assertEqual(solution.canConstruct(ransomNote, magazine), False)
    
    def test_example_3(self):
        ransomNote = "aa"
        magazine = "aab"
        solution = Solution()
        self.assertEqual(solution.canConstruct(ransomNote, magazine), True)
    