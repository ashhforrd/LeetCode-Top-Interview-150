class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = 1

        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                
                upper = dp[i-1][j] if i != 0 else 0
                left = dp[i][j-1] if j != 0 else 0

                dp[i][j] = upper + left
        
        return dp[-1][-1]