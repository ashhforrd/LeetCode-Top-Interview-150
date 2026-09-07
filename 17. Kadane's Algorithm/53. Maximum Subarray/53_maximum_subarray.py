class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        summary = 0

        for n in nums:
            summary += n

            maximum = max(maximum, summary)

            if summary < 0:
                summary = 0

        return maximum