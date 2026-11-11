class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1

        sumMax = float('-inf')
        while left < right:
            sumMax = max(sumMax, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return sumMax
