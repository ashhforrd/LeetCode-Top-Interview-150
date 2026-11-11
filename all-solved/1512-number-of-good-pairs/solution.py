class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    res += 1
        
        return res
