from src.katas.numberOfOneBit import Solution
from unittest import TestCase


class TestNumberOfOneBit(TestCase):

    def test_searchInEleven(self):
        n = 11
        solution = Solution()
        self.assertEqual(solution.hammingWeight(n), 3)
    
    def test_searchInThreeDigit(self):
        n = 128
        solution = Solution()
        self.assertEqual(solution.hammingWeight(n), 1)

    def test_searchInTenDigit(self):
        n = 2147483645
        solution = Solution()
        self.assertEqual(solution.hammingWeight(n), 30)

    def test_searchInEleven(self):
        n = 11
        solution = Solution()
        self.assertEqual(solution.hammingWeightWithUsingAndOperator(n), 3)
    
    def test_searchInThreeDigit(self):
        n = 128
        solution = Solution()
        self.assertEqual(solution.hammingWeightWithUsingAndOperator(n), 1)

    def test_searchInTenDigit(self):
        n = 2147483645
        solution = Solution()
        self.assertEqual(solution.hammingWeightWithUsingAndOperator(n), 30)

