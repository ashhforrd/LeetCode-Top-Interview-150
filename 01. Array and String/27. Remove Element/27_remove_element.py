class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                if nums[right] == val:
                    right -= 1
                else:
                    nums[left] = nums[right]
                    nums[right] = val
                    left += 1
                    right -= 1
            else:
                left += 1
        
        return left