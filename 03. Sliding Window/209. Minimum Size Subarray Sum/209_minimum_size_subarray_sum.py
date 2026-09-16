class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = float('inf')

        summary = 0

        for right in range(len(nums)):
            summary += nums[right]

            while summary >= target:
                minLen = min(minLen, right - left + 1)
                summary -= nums[left]
                left += 1

        return minLen if minLen != float('inf') else 0