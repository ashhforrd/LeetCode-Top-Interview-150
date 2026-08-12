class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        currentEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                currentEnd = farthest
                jump += 1
        
        return jump