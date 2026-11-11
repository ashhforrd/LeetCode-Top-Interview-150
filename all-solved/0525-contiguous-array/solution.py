class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSum = 0
        binaryMap = { 0: -1 }
        longest = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefixSum -= 1
            else:
                prefixSum += 1
            
            if prefixSum in binaryMap:
                longest = max(longest, i - binaryMap[prefixSum])
            else:
                binaryMap[prefixSum] = i
            
        return longest
