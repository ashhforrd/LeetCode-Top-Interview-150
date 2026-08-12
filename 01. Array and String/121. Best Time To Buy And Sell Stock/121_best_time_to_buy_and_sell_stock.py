class Solution:
    def maxProfit(self, prices: List[int]) -> int:             
        # minPrice = prices[0]
        # profit = 0

        # for price in prices[1:]:
        #     minPrice = min(minPrice, price)
        #     profit = max(profit, price - minPrice)
        
        # return profit

        dp_profit = [0] * len(prices)
        min_price = prices[0]

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])

            dp_profit[i] = max(dp_profit[i-1], prices[i] - min_price)
        
        return dp_profit[-1]
