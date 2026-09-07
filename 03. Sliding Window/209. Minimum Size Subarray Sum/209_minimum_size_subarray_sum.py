class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_length = 10 ** 9

        total = 0

        while right < len(nums):
            total += nums[right]

            while total >= target:
                min_length = min(right - left + 1, min_length)
                total -= nums[left]
                left += 1
            
            right += 1

        return min_length if min_length != 10 ** 9 else 0