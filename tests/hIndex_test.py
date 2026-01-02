from src.katas.hIndex import Solution
from unittest import TestCase


class TestHIndex(TestCase):

    def test_case_1(self):
        citations = [3,0,6,1,5]

        solution = Solution()
        self.assertEqual(solution.hIndex(citations), 3)
    
    def test_case_2(self):
        citations = [1,2,3,4,5]

        solution = Solution()
        self.assertEqual(solution.hIndex(citations), 3)
    
    def test_case_3(self):
        citations = [1,3,1]

        solution = Solution()
        self.assertEqual(solution.hIndex(citations), 1)