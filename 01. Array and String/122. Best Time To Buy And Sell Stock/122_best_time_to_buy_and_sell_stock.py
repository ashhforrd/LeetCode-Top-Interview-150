class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            
            profit = prices[right] - prices[left]
            
            if profit > 0:
                max_profit += profit
                left = right
        
        return max_profit