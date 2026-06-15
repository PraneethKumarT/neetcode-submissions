class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for n in prices:
            if n < buy:
                buy = n
            profit = max(profit, n-buy)
        
        return profit

        