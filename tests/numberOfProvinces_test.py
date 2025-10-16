from src.katas.numberOfProvinces import Solution
from unittest import TestCase


class TestNumberOfProvinces(TestCase):

    def test_output_2(self):
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        solution = Solution()
        self.assertEqual(solution.findCircleNum(isConnected), 2)
    
    def test_three_indiviual_nodes(self):
        isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        solution = Solution()
        self.assertEqual(solution.findCircleNum(isConnected), 3)
    
    def test_additional_1(self):
        isConnected = [[1,1,0],[1,0,0],[0,0,1]]
        solution = Solution()
        self.assertEqual(solution.findCircleNum(isConnected), 2)
    