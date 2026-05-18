class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell, buy = len(prices)-1,len(prices)-1
        while sell > 0:
            profit = max(profit, prices[sell]-prices[buy])
            if buy > 0:
                buy -= 1
            else:
                sell -= 1
                buy = sell-1
        return profit