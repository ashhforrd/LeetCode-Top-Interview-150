class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp1 = [0] * len(nums) # 0 ... n - 1
        dp2 = [0] * len(nums) # 1 ... n
        
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])
        
        dp2[0] = 0
        dp2[1] = nums[1]
        for j in range(2, len(nums)):
            dp2[j] = max(dp2[j - 1], nums[j] + dp2[j - 2])

        return max(dp1[-2], dp2[-1])
