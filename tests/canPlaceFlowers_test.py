from src.katas.canPlaceFlowers import Solution
from unittest import TestCase


class TestCanPlaceFlowers(TestCase):

    def test_n_1(self):
        flowerbed = [1,0,0,0,1]
        n = 1
        solution = Solution()
        self.assertEqual(solution.canPlaceFlowers(flowerbed, n), True)
    
    def test_n_2(self):
        flowerbed = [1,0,0,0,1]
        n = 2
        solution = Solution()
        self.assertEqual(solution.canPlaceFlowers(flowerbed, n), False)

    def test_flowerbed_with_5_emptySpots(self):
        flowerbed = [1,0,0,0,0,1]
        n = 2
        solution = Solution()
        self.assertEqual(solution.canPlaceFlowers(flowerbed, n), False)
