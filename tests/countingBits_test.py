from unittest import TestCase
from src.katas.countingBits import Solution

class TestCountingBits(TestCase):

    def test_when_n_is_two(self):
        n = 2
        result = Solution()
        self.assertEqual(result.countBits(n), [0,1,1])

    def test_when_n_is_five(self):
        n = 5
        result = Solution()
        self.assertEqual(result.countBits(n), [0,1,1,2,1,2])