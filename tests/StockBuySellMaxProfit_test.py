# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from src.katas import StockBuySellX
import unittest
#class name and file name should be different
class StockBuySellMaxProfit_test(unittest.TestCase): 

    
    def test_BestTimeToBuyStock(self):

        # def should be filename.classname
        stockBuySell = StockBuySellX.StockBuySell()
        
        self.assertEqual(stockBuySell.maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(stockBuySell.maxProfit([7,6,4,3,1]), 0)
        self.assertEqual(stockBuySell.maxProfit([2,4,1]), 2)
        self.assertEqual(stockBuySell.maxProfit([2,1,2,1,0,1,2]), 2)


    #     class TwoSum_test(unittest.TestCase):
    # def test_TwoSum(self):
    #     solution=  twoSum.TwoSum()
 


# Given:
# We have an array of items.  Each of the items indicates the price of a stock on a given day.

# Goal/Objective:
# We need to calculate the possible maximum profit when we choose a day to buy the stock and sell on a different day in the future 

# Solution:
# To implement this, here is the logic. Compare the items in an array and find what day we should buy and sell the stock in the future to get maximum profit.

# Assumptions:
# •	We have to buy first and sell later. 
# •	This process should be done only once. 
# •	Since we are talking about the prices of a stock, the values are not negative





