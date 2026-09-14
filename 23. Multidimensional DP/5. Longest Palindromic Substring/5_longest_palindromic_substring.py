class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        start, end = 0, 1

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    
                    if dp[i][j] == True and j - i + 1 > end:
                        start = i
                        end = j - i + 1
                else:
                    dp[i][j] = False

        return s[start:start + end]