from src.katas.editDistance import Solution
from unittest import TestCase


class TestEditDistance(TestCase):

    def test_example_1(self):
        word1 = "horse"
        word2 = "ros"
        solution = Solution()
        self.assertEqual(solution.minDistance(word1,word2), 3)
    
    def test_example_2(self):
        word1 = "intention"
        word2 = "execution"
        solution = Solution()
        self.assertEqual(solution.minDistance(word1,word2), 5)
    
   