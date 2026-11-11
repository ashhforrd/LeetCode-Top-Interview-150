class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                left = dp[i - 1][j] if i > 0 else 0
                top = dp[i][j - 1] if j > 0 else 0
                diagonal = dp[i - 1][j - 1] if i > 0 and j > 0 else 0

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + diagonal
                else:
                    dp[i][j] = max(left, top)

        return dp[-1][-1]
