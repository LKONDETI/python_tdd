from src.katas.reverseBits import Solution
from unittest import TestCase


class TestReverseBits(TestCase):

    def test_case_1(self):
        n = 0b00000010100101000001111010011100
        solution = Solution()
        self.assertEqual(solution.reverseBits(n), 964176192)
        
    def test_case_2(self):
        n = 0b11111111111111111111111111111101
        solution = Solution()
        self.assertEqual(solution.reverseBits(n), 3221225471)
