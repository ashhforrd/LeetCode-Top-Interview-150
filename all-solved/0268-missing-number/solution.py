class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        last_num = max(max(nums), len(nums))
        total_sum = last_num * (last_num + 1) // 2

        return total_sum - sum(nums)
