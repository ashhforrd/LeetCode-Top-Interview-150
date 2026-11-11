class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        number = {}
        for n in nums:
            number[n] = number.get(n, 0) + 1
                        
        dp = [0] * len(number)
        keys = sorted(number)

        for i, key in enumerate(keys):
            points = key * number[key]

            if i == 0:
                dp[0] = points
            elif key == keys[i - 1] + 1:
                take = points + (dp[i - 2] if i >= 2 else 0)
                skip = dp[i - 1]
                dp[i] = max(take, skip)
            else:
                dp[i] = points + dp[i - 1]

        return dp[-1]
