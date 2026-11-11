class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        total = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                        total += 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                        if dp[i][j]:
                            total += 1
                else:
                    dp[i][j] = False
        
        return total
