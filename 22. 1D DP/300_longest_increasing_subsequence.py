class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            # Mencari angka yang lebih kecil dari nums[i] dan memiliki value terbesar
            longest = 1
            for j in range(i):
                if nums[j] < nums[i]: 
                    longest = max(longest, 1 + dp[j])
            dp[i] = longest
        
        print(dp)

        return max(dp)