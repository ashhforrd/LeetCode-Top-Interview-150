class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # index = 0
        # found = True

        # if target in nums:
        #     index = nums.index(target)
        # else:
        #     for i in range(len(nums)):
        #         if target < nums[i]:
        #             index = i
        #             return index
      
        #     index = len(nums)

        # return index
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            
            if nums[mid] == target:
                return mid

        return left
