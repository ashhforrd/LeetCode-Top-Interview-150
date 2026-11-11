class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        # def backtrack(nums, x, ops):
        #     if x == 0:
        #         return ops

        #     if nums == [] or x < 0:
        #         return -1
            
        #     left = backtrack(nums[1:], x - nums[0], ops + 1) 
        #     right = backtrack(nums[:len(nums) - 1], x - nums[-1], ops + 1)

        #     return min(left, right) if left != -1 and right != -1 else max(left, right)
      
        # return backtrack(nums, x, 0) 

        operations = float('inf')
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        l = 0
        windowSum = 0

        for r in range(len(nums)):
            windowSum += nums[r]

            while l < len(nums) and windowSum >= target:
                if windowSum == target:
                    operations = min(operations, len(nums) - (r - l + 1))

                windowSum -= nums[l]
                l += 1
        
        return operations if operations != float('inf') else -1
