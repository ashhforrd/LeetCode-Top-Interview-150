class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        dp = [
            [[float('-inf')] * 2 for _ in range(k + 1)]
            for _ in range(len(prices))
        ]

        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k + 1):
                
                dp[i][j][0] = dp[i - 1][j][0]

                if j > 0:
                    dp[i][j][0] = max(
                        dp[i][j][0],
                        dp[i - 1][j - 1][1] + prices[i]
                    )
                
                dp[i][j][1] = max(
                    dp[i - 1][j][1],
                    dp[i - 1][j][0] - prices[i]
                )
        
        return max(dp[-1][j][0] for j in range(k + 1))