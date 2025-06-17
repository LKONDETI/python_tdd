from src.katas.guessNumberLowerOrHigher import Solution
from unittest import TestCase


class TestGuessNumberLowerOrHigher(TestCase):

    def test_output_6(self):
        n = 10
        pick = 6
        solution = Solution()
        self.assertEqual(solution.guessNumber(n,pick), 6)
    
    def test_output_1(self):
        n = 1
        pick = 1
        solution = Solution()
        self.assertEqual(solution.guessNumber(n, pick), 1)
    
    def test_output_1_when_n_2(self):
        n = 2
        pick = 1
        solution = Solution()
        self.assertEqual(solution.guessNumber(n, pick), 1)