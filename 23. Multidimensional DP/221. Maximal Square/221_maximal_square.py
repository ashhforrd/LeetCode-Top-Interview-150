class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M = len(matrix) 
        N = len(matrix[0]) 

        maximum = 0
        dp = [[0 for _ in range(N)] for _ in range(M)]

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        left = dp[i][j - 1]
                        top = dp[i - 1][j]
                        top_left = dp[i - 1][j - 1]
                
                        dp[i][j] = min(left, top, top_left) + 1

                    maximum = max(maximum, dp[i][j])
                
        return maximum * maximum