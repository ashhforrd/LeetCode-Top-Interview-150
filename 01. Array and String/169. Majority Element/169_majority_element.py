class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2

        nums.sort()
        return nums[majority_count]