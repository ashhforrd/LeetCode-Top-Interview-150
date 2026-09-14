class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                
                upper = dp[i-1][j] if i != 0 else 0
                left = dp[i][j-1] if j != 0 else 0

                if i != 0 and j != 0:
                    dp[i][j] += grid[i][j] + min(upper, left)
                else:
                    dp[i][j] += grid[i][j] + left + upper
        
        return dp[-1][-1]