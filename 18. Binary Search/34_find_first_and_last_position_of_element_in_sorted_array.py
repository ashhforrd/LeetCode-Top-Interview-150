class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # mencari start dan end index dari target, binary search di index

        left = 0
        right = len(nums)-1

        start = -1
        end = -1

        while left <= right:
            mid = left + (right - left) // 2 

            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1 
        
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2 

            if nums[mid] == target:
                end = mid
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return [start, end]