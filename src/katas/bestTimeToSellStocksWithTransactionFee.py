from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        hold = -prices[0]
        cash = 0
        for i in range(n):
            prev_cash = cash
            prev_hold = hold
            hold = max(prev_hold, prev_cash - prices[i])
            cash = max(prev_cash, prev_hold + prices[i] - fee)
        return cash

