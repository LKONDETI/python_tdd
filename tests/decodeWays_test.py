from src.katas.decodeWays import Solution
from unittest import TestCase


class TestDecodeWays(TestCase):

    def test_string_of_two(self):
        s = "12"
        solution = Solution()
        self.assertEqual(solution.numDecodings(s), 2)
    
    def test_string_of_three(self):
        s = "226"
        solution = Solution()
        self.assertEqual(solution.numDecodings(s), 3)

    def test_string_of_containing_zero(self):
        s = "06"
        solution = Solution()
        self.assertEqual(solution.numDecodings(s), 0)
