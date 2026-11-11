class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l, r = 0, 0

        longest = 0
        zeros = 0
    
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                
                l += 1
            
            longest = max(longest, r - l)
        
        return longest
