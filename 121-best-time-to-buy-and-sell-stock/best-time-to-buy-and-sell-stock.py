class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        minimum_buy = prices[0]
        for price in prices:
            if minimum_buy > price:
                minimum_buy = price
            elif price - minimum_buy > max_profit:
                max_profit = price - minimum_buy
                
        return max_profit