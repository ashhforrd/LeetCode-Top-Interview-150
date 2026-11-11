class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)

        # dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        # q = deque()

        # for j in range(n):
        #     q.append((0, j, matrix[0][j]))
        #     dp[0][j] = matrix[0][j]
        
        # res = float('inf')

        # while q:
        #     i, j, sums = q.popleft()

        #     for k in range(j - 1, j + 2):
        #         if 0 <= k <= n - 1 and i < n - 1:
        #             newSum = sums + matrix[i + 1][k]

        #             if newSum >= dp[i + 1][k]:
        #                 continue
                    
        #             dp[i + 1][k] = newSum

        #             if i + 1 == n - 1:
        #                 res = min(res, sums + newSum])
        #             else:
        #                 q.append((i + 1, k, newSum))

        
        # return res if res != float('inf') else min(matrix[0])

        dp = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + (min(
                    dp[i - 1][j - 1] if j > 0 else float('inf'),
                    dp[i - 1][j],
                    dp[i - 1][j + 1] if j < n - 1 else float('inf'),
                ) if 0 < i < n else 0)
        
        return min(dp[-1])
