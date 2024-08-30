from src.katas.containerWithMaxWater import Solution
from unittest import TestCase


class TestContainerWithMaxWater(TestCase):

    def test_AreaWithMultipleHeights(self):
        height = [1,8,6,2,5,4,8,3,7]
        solution = Solution()
        self.assertEqual(solution.maxArea(height), 49)

    def test_AreaWhenTheHeightsAreOne(self):
        height = [1,1]
        solution = Solution()
        self.assertEqual(solution.maxArea(height), 1)

