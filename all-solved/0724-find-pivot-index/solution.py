class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum, rightSum = 0, sum(nums)

        for i in range(0, len(nums)):
            leftSum += nums[i - 1] if i > 0 else 0
            rightSum -= nums[i]
        
            if leftSum == rightSum:
                return i
        
        return -1
