from src.katas.bestTimeToSellStocksWithTransactionFee import Solution
import unittest

class bestTimeToSellStocksWithTransactionFee(unittest.TestCase): 
  
    def test_example_1(self):

        # prices = [1,3,2,8,4,9], fee = 2
        result = Solution()
        self.assertEqual(result.maxProfit([1,3,2,8,4,9],2), 8)
    
    def test_example_2(self):
        result = Solution()
        self.assertEqual(result.maxProfit([1,3,7,5,10,3],3), 6)
    

    