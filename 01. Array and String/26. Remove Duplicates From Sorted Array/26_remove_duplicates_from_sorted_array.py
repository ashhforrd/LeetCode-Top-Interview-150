class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[left-1]:
                nums[left] = nums[right]
                left += 1
        
        return left