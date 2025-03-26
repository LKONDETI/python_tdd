from src.katas.reverseWordsOfString import Solution
from unittest import TestCase


class TestReverseWordsOfString(TestCase):

    def test_example_1(self):
        s = "the sky is blue"
        solution = Solution()
        self.assertEqual(solution.reverseWords(s), "blue is sky the")
    
    def test_example_2(self):
        s = "  hello world  "
        solution = Solution()
        self.assertEqual(solution.reverseWords(s), "world hello")
    
    def test_example_3(self):
        s = "a good   example"
        solution = Solution()
        self.assertEqual(solution.reverseWords(s), "example good a")