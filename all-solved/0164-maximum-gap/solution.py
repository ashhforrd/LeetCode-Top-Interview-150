class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        # if n < 2:
        #     return 0
        nums.sort()
        maxDiff = 0

        left, right = 0, 1
        while right < len(nums):
            diff = nums[right] - nums[left]
            maxDiff = max(maxDiff, diff)
            left += 1
            right += 1

        return maxDiff
