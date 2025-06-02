from unittest import TestCase
from src.katas.removingStarsfromString import Solution

class TestRemovingStarsfromString(TestCase):

    def test_leetcode(self):
        s = "leet**cod*e"
        result = Solution()
        self.assertEqual(result.removeStars(s), "lecoe")
    
    def test_abcd(self):
        s = "abcd"
        result = Solution()
        self.assertEqual(result.removeStars(s), "abcd")
    
    def test_empty_string(self):
        s = "erase*****"
        result = Solution()
        self.assertEqual(result.removeStars(s), "")