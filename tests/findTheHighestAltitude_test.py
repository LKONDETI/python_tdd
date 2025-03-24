from src.katas.findTheHighestAltitude import Solution
from unittest import TestCase


class TestFindTheHighestAltitude(TestCase):

    def test_output_1(self):
        gain = [-5,1,5,0,-7]
        solution = Solution()
        self.assertEqual(solution.largestAltitude(gain), 1)
    
    def test_output_0(self):
        gain = [-4,-3,-2,-1,4,3,2]
        solution = Solution()
        self.assertEqual(solution.largestAltitude(gain), 0) 