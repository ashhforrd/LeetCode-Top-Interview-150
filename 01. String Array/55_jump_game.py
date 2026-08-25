class Solution:
    def canJump(self, nums: List[int]) -> bool:
        position = 0
        n = len(nums)

        if n == 1:
            return True
        
        if nums[0] == 0:
            return False
       
        target = n - 1
        current = 0

        while current <= position:
            if position >= target:
                return True
            position = max(current + nums[current], position)
            current += 1
        
        return False