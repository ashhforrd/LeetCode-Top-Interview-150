class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort()
        
        dp = [0] * len(pairs)
        dp[0] = 1

        for i in range(1, len(pairs)):
            longest = 1
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    longest = max(longest, 1 + dp[j])
            dp[i] = longest

        return max(dp)
