from typing import List

class StockBuySell:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit


# here list of the integers are named as prices, the minimum price is index{0} and maxprofit is assigned as 0. 
# here in the 'for' loop price is starting with index{1}. So max_profit is max(max_profit,price-min_profit) 
# where the value is compared. max() function compares and displaces the maximum value. price-min_price is index{1}-index{0} same goes with the other integers in the list
# and min_price always get update of the minimum value of the min_price(that is the intial value) and price is the updated value in the loop