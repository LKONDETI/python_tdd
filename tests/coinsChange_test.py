from unittest import TestCase
from src.katas.coinChange import Solution

class TestCoinsChange(TestCase):

    def test_single_item_2(self):
        coins = [2]
        result = Solution()
        self.assertEqual(result.coinChangeTopDown(coins, 3), -1)

    def test_single_item_1(self):
        coins = [1]
        result = Solution()
        self.assertEqual(result.coinChangeTopDown(coins, 0),0)

    def test_multiple_items(self):
        coins = [1, 2, 5]
        result = Solution()
        self.assertEqual(result.coinChangeTopDown(coins, 11),3)

    def test_single_item_2_using_BottomUpApproch(self):
        coins = [2]
        result = Solution()
        self.assertEqual(result.coinChangeBottomUp(coins, 3), -1)

    def test_single_item_1_using_BottomUpApproch(self):
        coins = [1]
        result = Solution()
        self.assertEqual(result.coinChangeBottomUp(coins, 0),0)

    def test_multiple_items_using_BottomUpApproch(self):
        coins = [1, 2, 5]
        result = Solution()
        self.assertEqual(result.coinChangeBottomUp(coins, 11),3)
    
    