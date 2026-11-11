class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1

        while right < len(nums): 
            if nums[left] == 0:
                if nums[right] == 0:
                    right += 1
                else:
                    nums[left] = nums[right]
                    nums[right] = 0
                    left += 1
                    right += 1
            else:
                left += 1
                right += 1
