class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        nums = [x for x in nums if x >= 0]
        nums.insert(0, 0) # depannya 0

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                return nums[i] + 1

        return nums[len(nums)-1]+1
