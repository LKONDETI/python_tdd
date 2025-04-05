from src.katas.kidsWithTheGreatestNumberOfCandies import Solution
from unittest import TestCase


class TestKidsWithTheGreatestNumberOfCandies(TestCase):

    def test_example_1(self):
        candies = [2,3,5,1,3]
        extraCandies = 3
        output = [True,True,True,False,True]
        solution = Solution()
        self.assertEqual(solution.kidsWithCandies(candies, extraCandies), output)

    def test_example_2(self):
        candies = [4,2,1,1,2]
        extraCandies = 1
        output = [True,False,False,False,False]
        solution = Solution()
        self.assertEqual(solution.kidsWithCandies(candies, extraCandies), output)

    def test_example_3(self):
        candies = [12,1,12]
        extraCandies = 10
        output = [True,False,True]
        solution = Solution()
        self.assertEqual(solution.kidsWithCandies(candies, extraCandies), output)