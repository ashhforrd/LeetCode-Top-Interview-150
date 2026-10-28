class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1

                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1

                left -= 1
                right += 1
        
        return res

        # n = len(s)
        # dp = [[False for _ in range(n)] for _ in range(n)]
        
        # start, end = 0, 1

        # for i in range(n-1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j]:
        #             if j - i <= 2:
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = dp[i+1][j-1]
                    
        #             if dp[i][j] == True and j - i + 1 > end:
        #                 start = i
        #                 end = j - i + 1
        #         else:
        #             dp[i][j] = False

        # return s[start:start + end]
