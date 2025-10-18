from src.katas.reorderRoutesToMakeAllPathsLeadToCityZero import Solution
from unittest import TestCase


class TestReorderRoutesToMakeAllPathsLeadToCityZero(TestCase):

    def test_case_1(self):
        n = 6
        connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        solution = Solution()
        self.assertEqual(solution.minReorder(n,connections), 3)
    
    def test_case_2(self):
        n = 5
        connections = [[1,0],[1,2],[3,2],[3,4]]
        solution = Solution()
        self.assertEqual(solution.minReorder(n,connections), 2)
    
    def test_case_3(self):
        n = 3
        connections = [[1,0],[2,0]]
        solution = Solution()
        self.assertEqual(solution.minReorder(n,connections), 0)