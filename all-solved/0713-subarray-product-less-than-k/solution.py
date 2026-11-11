class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        res = 0
        prod = 1

        left = 0
        for right in range(len(nums)):
            prod *= nums[right]

            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1

            res += (right - left + 1)
        
        return res
