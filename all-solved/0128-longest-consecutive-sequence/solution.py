class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 0:
            return 0

        longest, current = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue

            if nums[i] - nums[i-1] == 1:
                current += 1
            else:
                current = 1
            
            longest = max(current, longest)
                
        return longest
