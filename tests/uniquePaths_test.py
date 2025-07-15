from src.katas.uniquePaths import Solution
from unittest import TestCase


class TestUniquePaths(TestCase):

    def test_example1(self):
        m = 3
        n = 7
        solution = Solution()
        self.assertEqual(solution.uniquePaths(m,n), 28)
    
    def test_example2(self):
        
        solution = Solution()
        self.assertEqual(solution.uniquePaths(3,2), 3)
    
    def test_single_row(self):
        m = 1
        n = 5
        solution = Solution()
        self.assertEqual(solution.uniquePaths(m,n), 1)