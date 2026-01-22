from src.katas.reverseInteger import Solution
from unittest import TestCase


class TestReverseInteger(TestCase):

    def test_case_1(self):
        n = 123
        solution = Solution()
        self.assertEqual(solution.reverse(n), 321)

    def test_case_2(self):
        n = -123
        solution = Solution()
        self.assertEqual(solution.reverse(n), -321)

    def test_case_3(self):
        n = 120
        solution = Solution()
        self.assertEqual(solution.reverse(n), 21)

    def test_case_4(self):
        n = 0
        solution = Solution()
        self.assertEqual(solution.reverse(n), 0)

    def test_case_5(self):
        n = 1534236469
        solution = Solution()
        self.assertEqual(solution.reverse(n), 0)
