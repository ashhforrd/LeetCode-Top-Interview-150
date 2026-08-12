class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left = 2

        for right in range(2, len(nums)):
            if nums[right] != nums[left-2]:
                nums[left] = nums[right]
                left += 1

        return left